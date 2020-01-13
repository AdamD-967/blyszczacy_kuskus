x = int(input("podaj liczbe (int)"))
z = int(input("podaj ilość cyfr znaczących"))
n = 0
X = []
for i in range(len(str(x))):
    X.append(int(str(x)[n]))
    n = n+1
if X[z] >= 5:
    X[z-1] = X[z-1]+1
q = 1
for j in range(len(X)-z):
    X[(z-1)+q] = 0
    q = q+1
o = ""
for k in X:
    o = o+str(k)
print(int(o))
