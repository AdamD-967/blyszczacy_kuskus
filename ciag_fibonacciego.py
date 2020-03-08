import time

print("program wypisuje ciąg fibonacciego")
x = int(input("podaj ilość elementów: "))

t1 = time.perf_counter()


def n(m):
    if m < 0:
        raise ValueError
    if m < 2:
        return 1
    else:
        return n(m-1)+n(m-2)


m = 1
for i in range(x):
    print(n(m))
    m = m+1

t2 = time.perf_counter()
print("czas pracy: ", t2-t1)
