import time
from numba import njit, int32

print("program wypisuje ciąg fibonacciego")
x = int(input("podaj ilość elementów: "))

t1 = time.perf_counter()


@njit(int32(int32))
def fib(m):
    if m < 0:
        raise ValueError
    if m < 2:
        return 1
    else:
        return fib(m-1)+fib(m-2)


m = 1
for i in range(x):
    print(fib(m))
    m = m+1

t2 = time.perf_counter()
print("czas pracy: ", t2-t1)
