import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import random
from itertools import count

x = list()
y = list()

it = count()

def animation(i):
    x.append(next(it))
    y.append(random.choice(x))
    plt.plot(x, y, color='blue')

an = FuncAnimation(plt.gcf(), animation, interval=1000)
plt.show()