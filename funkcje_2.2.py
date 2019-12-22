def f(L):
    P=[]
    for x in L:
        if x%2==0:
            P.append(x)
    return P


L=[]
a=int(input("podaj ilość elementów"))
for i in range(a):
    z=int(input("podaj element"))
    L.append(z)
print(f(L))
