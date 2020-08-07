import numpy as np
from scipy.constants import G
from numba import vectorize

dt = 0.01

class Obj():
    def __init__(self, r0: np.ndarray, v0: np.ndarray, mass: float):
        self.r = r0
        self.v = v0
        self.mass = mass

    def getacc(self, m: float, dr: np.ndarray):
        return G*m*dr/np.sqrt(dr[0]**2+dr[1]**2)**3

    def __repr__(self):
        return f"\ncrds: {self.r}\tv: {self.v}\tmass: {self.mass}"

class Env():
    def __init__(self, _all: np.ndarray):
        self.ALL = _all
        self.MASS: int = vectorize(lambda o: o.m)(self.ALL).sum()
        self.R: int = vectorize(lambda o: o.r)(self.ALL).sum()

    @vectorize
    def update(self):
        dm, dr = self.MASS-self.ALL.mass, self.ALL.R-self.ALL.r
        acc = self.ALL.getacc(dm, dr)
        self.ALL.r += self.ALL.v*dt
        self.ALL.v += acc*dt
    
    def run(self, it):
        for _ in range(it):
            self.update()

    def __repr__(self):
        return self.ALL