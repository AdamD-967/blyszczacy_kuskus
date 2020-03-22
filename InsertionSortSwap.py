def swap(arr, s, f):
    n = arr[s]
    for i in range(f, s+1):
        n, arr[i] = arr[i], n


L = [1, 5, 9, 7, 6]
print(L)
a1 = int(input("si: "))-1
a2 = int(input("fi: "))-1
swap(L, a1, a2)
print(L)
