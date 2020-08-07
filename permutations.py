from numba import njit

@njit
def perm(s: list, a: int) -> list:
    n: int = len(s)
    test: list = [n-1 for _ in range(a)]
    it: list = [0 for _ in range(a)]

    while it != test:
        yield [s[j] for j in it]
        it[0] += 1
        for i in range(a-1):
            if (it[i] == n):
                it[i] = 0
                it[i+1] += 1
    yield [s[j] for j in test]

p = perm([i for i in range(int(input('zakres: ')))], int(input('liczba elementów: ')))

for i in p:
    print(i)
