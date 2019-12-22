def f(L):
    x = 0
    for element in L:
        x += element
    return x


L = []
a = int(input("dawka elementów"))
for i in range(a):
    y = int(input("podaj zmienną"))
    L.append(y)
print(f(L))