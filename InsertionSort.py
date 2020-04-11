import random

def Isort(arr):
    for i in range(len(arr)):
        n = arr[i]
        j = i-1
        for j in range(i-1, -1, -1):
            if arr[j] > arr[i]:
                arr.insert(j, arr.pop(i))
                break


L = []
l = int(input("podaj ilość elementów: "))
a1 = int(input("podaj początek zakresu: "))
a2 = int(input("podaj koniec zakresu: "))
for r in range(l):
    L.append(random.randint(a1, a2))
print(L)
Isort(L)
print(L)
