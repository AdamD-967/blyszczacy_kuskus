import matplotlib.pyplot as plt
import numpy as np
from Equation import Expression

f = Expression(input("podaj wzór funkcji"), ["x"])
x = np.arange(0, 10, 0.1)
plt.plot(x, f(x), "g*", label=str(f))
plt.legend()
plt.grid()
plt.axvline(color="k", lw=2)
plt.axhline(color="k", lw=2)
plt.show()