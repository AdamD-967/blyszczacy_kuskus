#a split dzieli, nie łączy
def f(a, b, c):
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    else:
        return c


c=int(input("daj c"))
b=int(input("daj b"))
a=int(input("daj a"))
print(f(a, b, c))