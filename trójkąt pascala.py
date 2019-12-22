x=int(input("podaj ilość rzędów"))
y=1
def i(n):
    return n+1
n=0
for w in range(x):
    if i(n)==1:
        m=1
    else:
        m=0
    print(i(n),":",m)
    n=n+1
    f=i(n)
def m(f):
    return i(n-1)+i(n-2)
for z in range(x):
    print(i(n),":",m(f))