import matplotlib.pyplot as plt

X = []
Y = []
n = input('rysować? (r-tak)')
while n == "r":
    if n != "r":
        break
    a = int(input("dawka współrzędnych"))
    for i in range(a):
        x = int(input("podaj wps.x"))
        X.append(x)
        y = int(input("podaj wsp.y"))
        Y.append(y)

    plt.plot(X, Y, input("kolor i narzędzie"))
    plt.show()
    n = input('rysować dalej? (r-tak)')