x = int(input("podaj ilość elementów"))
y = int(input("podaj ilość kombinacji"))
X = []
Y = []
for i in range(x):
    a = int(input("podaj element"))
    X.append(a)
for i in range(y):
    Y.append(0)
n = 0
m = 1
while n < len(X)-1:
    while m < len(X)-1:
        if X[n] == X[m]:
            X.remove(X[m])
        m = m+1
    m = 1
    n = n+1
s = 1
w = len(X)**len(Y)
W = []