from numba import float64
from numba.experimental import jitclass
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

dt = 0.01
g = 9.81

spec = [
    ('v', float64), 
    ('l', float64), 
    ('h', float64), 
    ('m', float64), 
    ('k', float64), 
    ('t', float64), 
    ('b', float64), 
    ('l', float64)
]
@jitclass(spec)
class Env:
    def __init__(self, h0: float, m: float, k: float, b: float, l: float):
        self.v = 0.0
        self.h = h0
        self.m = m
        self.k = k
        self.t = 0.0
        self.b = b
        self.l = l

    def update(self):
        if self.h <= self.l:
            ft = self.b*self.v
            fs = -self.h*self.k
            accs = fs-ft/self.m
            acc = accs-g
            self.v += acc*dt
            self.h += self.v*dt
        else:
            self.h = self.l
            self.v *= -1
        self.t += dt

    def run(self, it: int):
        for _ in range(it):
            self.update()
            yield self.t, self.h

l = float(input("l: "))
h = float(input("h: "))
m = float(input("m: "))
k = float(input("k: "))
b = float(input("b: "))
it = int(input("it: "))

env = Env(h, m, k, b, l)
process = env.run(it)

plt.style.use("fivethirtyeight")
def anim(i):
    x, y = next(process)
    plt.scatter([x], [y])

ani = FuncAnimation(plt.gcf(), anim, interval=1, repeat=False)
plt.tight_layout()
plt.show()
