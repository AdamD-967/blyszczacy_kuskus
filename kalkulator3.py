print("to jest kalkulator")
c = input("liczyć?")
a = float(input("podaj a"))
while c == "tak":
    if c != "tak":
        break
    b = float(input("podaj b"))
    print(b)
    d = int(input("""wybierz działanie:
    1.iloczyn,
     2.iloraz,
      3.suma,
       4.różnica,
        5.potęga,
         6.pierwiastek"""))
    if d == 1:
        print(a * b)
        a = a * b
    elif d == 2:
        print(a / b)
        a = a / b
    elif d == 3:
        print(a + b)
        a = a + b
    elif d == 4:
        print(a - b)
        a = a - b
    elif d == 5:
        print(a ** b)
        a = a ** b
    elif d == 6:
        print(a ** (1 / b))
        a = a ** (1 / b)
    else:
        print("error")
    c = input("liczyć dalej?")
print("end")