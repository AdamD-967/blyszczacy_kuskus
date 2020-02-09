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
    if (a in X) and (b in X) and (c in X):
        print('and the winner is X')
        break
    elif (d in X) and (e in X) and (f in X):
        print('and the winner is X')
        break
    elif (g in X) and (h in X) and (i in X):
        print('and the winner is X')
        break
    elif (a in X) and (e in X) and (i in X):
        print('and the winner is X')
        break
    elif (c in X) and (e in X) and (g in X):
        print('and the winner is X')
        break
    elif (a in O) and (b in O) and (c in O):
        print('and the winner is O')
        break
    elif (d in O) and (e in O) and (f in O):
        print('and the winner is O')
        break
    elif (g in O) and (h in O) and (i in O):
        print('and the winner is O')
        break
    elif (a in O) and (e in O) and (i in O):
        print('and the winner is O')
        break
    elif (c in O) and (e in O) and (g in O):
        print('and the winner is O')
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
