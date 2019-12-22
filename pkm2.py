import random
print("pa-pier-ka-mień-no-zi-cie")
L = ["papier", "kamień", "nożyce"]
w = 0
r = input("gramy dalej?")
while r == "tak":
    if r != "tak":
        break
    x = input("wybierz swoją broń")
    y = random.choice(L)
    if x == y:
        print("remis")
        w = w
    elif x != "papier" and x != "kamień" and x != "nożyce":
        print("error")
        w = w
    else:
        if x == "papier":
            if y == "nożyce":
                print("wygrałeś")
                w = w+1
            else:
                print("przegrałeś")
                w = w-1
        elif x == "kamień":
            if y == "papier":
                print("wygrałeś")
                w = w+1
            else:
                print("przegrałeś")
                w = w+1
        else:
            if y == "kamień":
                print("wygrałeś")
                w = w+1
            else:
                print("przegrałeś")
                w = w-1
    r = input("gramy dalej?")
print("twój wynik to:", w)
print("end")