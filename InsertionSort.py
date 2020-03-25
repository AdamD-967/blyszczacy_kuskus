import random

def Isort(arr):
    for i in range(1, len(arr)):
        a = i+1
        for q in range(0, i-1):
            if arr[q] < arr[i]:
                a = q
                break
        n = arr[i]
        for m in range(a, i+1):
            n, arr[i] = arr[i], n


L = []
l = int(input("podaj ilość elementów: "))
a1 = int(input("podaj początek zakresu: "))
a2 = int(input("podaj koniec zakresu: "))
for r in range(l):
    L.append(random.randint(a1, a2))
print(L)
Isort(L)
print(L)
