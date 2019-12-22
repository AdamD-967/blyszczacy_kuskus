import matplotlib.pyplot as plt
import numpy as np
from Equation import Expression

f = Expression(input("podaj wzór funkcji"), ["x"])
k = float(input("od kąta"))
m = float(input("do kąta"))
l = float(input("między kątami"))
x = np.arange(k, m, l)
plt.plot(x, f(x), "g*", label=str(f))
plt.legend()
plt.grid()
plt.axvline(color="k", lw=2)
plt.axhline(color="k", lw=2)
plt.show()
