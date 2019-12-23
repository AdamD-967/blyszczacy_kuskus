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
for i in range(r):
    f = Expression(input("podaj wzór funkcji"), ["x"])
    Y.append(f)
for f in Y:
    y = f(x)
    if n == "linia ciągła":
        plt.plot(x, y, label=str(f))
    else:
        plt.plot(x, y, 'g*', label=str(f))
plt.legend()
plt.grid()
plt.axvline(color="k", lw=2)
plt.axhline(color="k", lw=2)
plt.show()
