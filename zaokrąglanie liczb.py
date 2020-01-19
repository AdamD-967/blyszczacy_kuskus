x = float(input("podaj liczbę"))
z = int(input("podaj liczbę cyfr znaczących"))
p = input("przed czy za przecinkiem")
n = 0
X = []
for i in range(len(str(x))):
    X.append(str(x)[n])
    n = n+1
Xp = []
up = 0
uz = X.index('.')+1
while up < X.index('.'):
    Xp.append(int(X[up]))
    up = up+1
if p == 'p':
    print(Xp)
    if Xp[z] >= 5:
        Xp[z-1] = Xp[z-1]+1
    q = 1
    for j in range(len(Xp)-z):
        Xp[(z-1)+q] = 0
        q = q+1
    o = ""
    for k in Xp:
        o = o+str(k)
    o = o+'.0'
else:
    Xz = []
    for i in range(len(X)-uz):
        Xz.append(int(X[uz]))
        uz = uz+1
    if Xz[z] >= 5:
        Xz[z-1] = Xz[z-1]+1
    q = 1
    for j in range(len(Xz)-z):
        Xz[(z-1)+q] = 0
        q = q+1
    o = ""
    for k in Xp:
        o = o + str(k)
    o = o+'.'
    for l in Xz:
        o = o+str(l)
print(float(o))
