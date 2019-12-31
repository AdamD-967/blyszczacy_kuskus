x = int(input("ilość rzędów"))


def f(X):
    Y = []
    n = 0
    for element in X:
        y = element+X[n-1]
        n = n+1
        Y.append(y)
    return Y


X = [1]
for j in range(x-1):
    X.append(0)
Y = []
for element in X:
    if element != 0:
        Y.append(element)
print(Y)
for i in range(x-1):
    Y = []
    X = f(X)
    for element in X:
        if element != 0:
            Y.append(element)
    print(Y)
