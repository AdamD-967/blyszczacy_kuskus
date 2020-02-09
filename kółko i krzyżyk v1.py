import numpy as np
import random as rd
from sympy import symbols
t = input('wybierz tryb')
a, b, c, d, e, f, g, h, i = symbols("a, b, c, d, e, f, g, h, i")
P = np.array([a, b, c, d, e, f, g, h, i]).reshape(3, 3)
print(P)
L = [a, b, c, d, e, f, g, h, i]
X = []
O = []
while True:
    if a and b and c in X:
        print('and the winner is X')
        break
    elif d and e and f in X:
        print('and the winner is X')
        break
    elif g and h and i in X:
        print('and the winner is X')
        break
    elif a and e and i in X:
        print('and the winner is X')
        break
    elif c and e and g in X:
        print('and the winner is X')
        break
    elif a and b and c in O:
        print('and the winner is X')
        break
    elif d and e and f in O:
        print('and the winner is X')
        break
    elif g and h and i in O:
        print('and the winner is X')
        break
    elif a and e and i in O:
        print('and the winner is X')
        break
    elif c and e and g in O:
        print('and the winner is X')
        break
    xw = int(input('podaj numer wiersza'))-1
    xk = int(input('podaj numer kolumny'))-1
    while P[xw, xk] not in L:
        xw = int(input('podaj numer wiersza')) - 1
        xk = int(input('podaj numer kolumny')) - 1
    L.remove(P[xw, xk])
    X.append(P[xw, xk])
    P[xw, xk] = 'x'
    if t == "zią":
        ow = int(input('podaj numer wiersza')) - 1
        ok = int(input('podaj numer kolumny')) - 1
        while P[ow, ok] not in L:
            ow = int(input('podaj numer wiersza')) - 1
            ok = int(input('podaj numer kolumny')) - 1
        L.remove(P[ow, ok])
        O.append(P[ow, ok])
        P[ow, ok] = 'o'
    else:
        ow = rd.choice(range(0, 2))
        ok = rd.choice(range(0, 2))
        while P[ow, ok] not in L:
            ow = rd.choice(range(0, 2))
            ok = rd.choice(range(0, 2))
        L.remove(P[ow, ok])
        O.append(P[ow, ok])
        P[ow, ok] = 'o'
    print(P)
print('end')
