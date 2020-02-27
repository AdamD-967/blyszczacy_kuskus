import numpy as np
from random import randint
from sympy import symbols
t = input('wybierz tryb')
a, b, c, d, e, f, g, h, i = symbols("a, b, c, d, e, f, g, h, i")
P = np.array([a, b, c, d, e, f, g, h, i]).reshape(3, 3)
print(P)
L = [a, b, c, d, e, f, g, h, i]
X = []
N = []
p = 0
while True:
    xw = int(input('podaj numer wiersza(x)'))-1
    xk = int(input('podaj numer kolumny'))-1
    while P[xw, xk] not in L or xw > 2 or xk > 2 or xw < 0 or xk < 0:
        xw = int(input('podaj numer wiersza(x)')) - 1
        xk = int(input('podaj numer kolumny(x)')) - 1
    L.remove(P[xw, xk])
    X.append(P[xw, xk])
    P[xw, xk] = 'x'
    if p >= 2:
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
        elif (a in X) and (d in X) and (g in X):
            print('and the winner is X')
            break
        elif (b in X) and (e in X) and (h in X):
            print('and the winner is X')
            break
        elif (c in X) and (f in X) and (i in X):
            print('and the winner is X')
            break
    if t == "zią":
        ow = int(input('podaj numer wiersza(o)')) - 1
        ok = int(input('podaj numer kolumny(o)')) - 1
        while P[ow, ok] not in L or ow > 2 or ok > 2 or ow < 0 or ok < 0:
            ow = int(input('podaj numer wiersza(o)')) - 1
            ok = int(input('podaj numer kolumny(o)')) - 1
        L.remove(P[ow, ok])
        N.append(P[ow, ok])
        P[ow, ok] = 'o'
    else:
        ow = randint(0, 2)
        ok = randint(0, 2)
        while P[ow, ok] not in L:
            ow = randint(0, 2)
            ok = randint(0, 2)
        L.remove(P[ow, ok])
        N.append(P[ow, ok])
        P[ow, ok] = 'o'
    if p >= 2:
        if (a in N) and (b in N) and (c in N):
            print('and the winner is O')
            break
        elif (d in N) and (e in N) and (f in N):
            print('and the winner is O')
            break
        elif (g in N) and (h in N) and (i in N):
            print('and the winner is O')
            break
        elif (a in N) and (e in N) and (i in N):
            print('and the winner is O')
            break
        elif (c in N) and (e in N) and (g in N):
            print('and the winner is O')
            break
        elif (a in N) and (d in N) and (g in N):
            print('and the winner is O')
            break
        elif (b in N) and (e in N) and (h in N):
            print('and the winner is O')
            break
        elif (c in N) and (f in N) and (i in N):
            print('and the winner is O')
            break
    p += 1
    if len(L) == 0:
        print("draw")
        break
    print(P)
print('end')
