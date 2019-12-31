c = input("liczba dziesiętna(d), czy binarna(b)?")
if c == "d":
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
    w = ""
    n = len(f(x))-1
    for i in range(len(f(x))):
        w = w + f(x)[n]
        n = n-1
    print(w)
else:
    def f(x):
        i = 0
        X = []
        for j in range(len(x)):
            X.append(x[i])
            i = i+1
        y = 0
        for element in X:
            element = int(element)
            if element == 1:
                y = 2*y+1
            elif element == 0:
                y = 2*y
        return y
    x = input("podaj liczbę")
    print(f(x))
print("end")
