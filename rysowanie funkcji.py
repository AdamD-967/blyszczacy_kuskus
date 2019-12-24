import matplotlib.pyplot as plt
import numpy as np
from Equation import Expression

Y = []
r = int(input("ilość funkcji"))
k = float(input("od kąta"))
m = float(input("do kąta"))
l = float(input("między kątami"))
n = input("wybierz sposób rysowania")
x = np.arange(k, m, l)
plt.figure()
plt.axvline(color="k", lw=2)
plt.axhline(color="k", lw=2)
for i in range(r):
    f = Expression(input("podaj wzór funkcji"), ["x"])
    Y.append(f)
for f in Y:
    y = f(x)
    if n == "lc":
        plt.plot(x, y, label=f)
    else:
        plt.plot(x, y, 'g*', label=f)
plt.legend()
plt.grid()
plt.show()
