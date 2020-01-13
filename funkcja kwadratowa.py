print("program liczy cechy funkcji kwadratowej")
print("f(x)=ax^2+bx^1+cx^0")
a = float(input("podaj a "))
print("a=", a)
b = float(input("podaj b"))
print("b=", b)
c = float(input("podaj c"))
print("c=", c)
print(f"f(x)={a}x^2+{b}x^1+{c}x^0")
delta = b**2-4*a*c
print("delta=", delta)
if delta < 0:
    print("nie ma rozwiązania :(")
elif delta == 0:
    print("x=", -b/2*a)
else:
    print("x1=", (-b - delta ** (1 / 2)) / (2 * a))
    print("x2=", (-b + delta ** (1 / 2)) / (2 * a))
print("W=", -b/2*a, delta/4*a)
print("end")
