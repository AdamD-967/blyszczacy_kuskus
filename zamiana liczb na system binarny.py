def f(x):
    M = []
    while x > 0:
        if x % 2 == 0:
            M.append(str(0))
            x = x/2
        else:
            M.append(str(1))
            x = (x-1)/2
    return M


x = int(input("podaj liczbę"))
f(x).reverse()
w = ""
for element in f(x):
    w = w+element
print(w)
