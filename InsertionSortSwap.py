def swap(arr, s, f):
    n = arr[s]
    for i in range(f, s+1):
        n, arr[i] = arr[i], n


L = [1, 5, 9, 7, 6]
print(L)
t = bool(int(input("dalej: ")))
while t:
    a = int(input("z kąd: "))-1
    b = int(input("do kąd: "))-1
    swap(L, a, b)
    print(L)
    t = bool(int(input("dalej: ")))
