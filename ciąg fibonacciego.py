print("program wypisuje ciąg fibonacciego")


def n(m):
    if m == 1:
        return 0
    elif m <= 2:
        return 1
    else:
        return n(m-1)+n(m-2)


x = int(input("podaj ilość elementów"))
m = 1
for i in range(x):
    print(n(m))
    m = m+1
print("end")