import random
from numba import njit

@njit
def isort(arr):
    for i in range(1, len(arr)):
        if arr[i-1] > arr[i]:
            j = 0
            while arr[i] > arr[j]:
                j+=1
            arr.insert(j, arr[i])
            arr.pop(i+1)


L = []
l = int(input("podaj ilość elementów: "))
a1 = int(input("podaj początek zakresu: "))
a2 = int(input("podaj koniec zakresu: "))
for r in range(l):
    L.append(random.randint(a1, a2))
print(L)
isort(L)
print(L)
