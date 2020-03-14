import random

def Bsort(arr):
    c = 1
    n = len(arr)-1
    while c > 0:
        c = 0
        for i in range(n):
            if arr[i] > arr[i+1]:
                a = arr[i]
                arr[i] = arr[i+1]
                arr[i+1] = a
                c+=1


l = int(input("podaj ilość elementów: "))
a1 = int(input("podaj początek zakresu: "))
a2 = int(input("podaj koniec zakresu: "))
L = []
for s in range(l):
    L.append(random.randint(a1, a2))
print(L)
Bsort(L)
print(L)
