import numpy as np
from numba import float64
from numba.experimental import jitclass
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation

g = 9.81
dt = 0.01

spec = [
    ('r', float64[:]), 
    ('v', float64[:])
]
@jitclass(spec)
class Obj:
    def __init__(self, r0: np.ndarray, v0: np.ndarray):
        self.r = r0
        self.v = v0

    def update(self):
        acc = np.array([-g*n/np.abs(n) if n else 0 for n in self.r])
        self.v += acc*dt
        self.r += self.v*dt

    def run(self, it: int):
        for _ in range(it):
            self.update()
            yield self.r


rx = float(input("rx: "))
ry = float(input("ry: "))
rz = float(input("rz: "))
vx = float(input("vx: "))
vy = float(input("vy: "))
vz = float(input("vz: "))
it = int(input("it: "))

obj = Obj(np.array([rx, ry, rz]), np.array([vx, vy, rz]))
src = obj.run(it)
datax = [rx]
datay = [ry]
dataz = [rz]

fig = plt.figure()
ax = Axes3D(fig)

plt.style.use("fivethirtyeight")
def animation(i):
    newx, newy, newz = next(src)
    datax.append(newx)
    datay.append(newy)
    dataz.append(newz)
    plt.cla()
    ax.scatter([0], [0], [0], color='red')
    ax.scatter([newx], [newy], [newz], color='green')
    ax.plot(datax, datay, dataz)

anim = FuncAnimation(fig, animation, interval=1, repeat=False)
plt.show()
