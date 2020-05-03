import random
from numba import njit

@njit
def ssort(v):
    for i in range(len(v)):
        n = v[i]
        for j in range(i, len(v)):
            if v[j] < n:
                n = v[j]
                a = j
        v[a] = v[i]
        v[i] = n


l = int(input("podaj ilość elementów: "))
a1 = int(input("podaj początek zakresu: "))
a2 = int(input("podaj koniec zakresu: "))
r = []
for m in range(l):
    r.append(random.randint(a1, a2))
print(r)
ssort(r)
print(r)
