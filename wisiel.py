import matplotlib.pyplot as plt
from random import randint
from csv import reader
print('zagrajmy w wiśła')
with open("some.txt") as c:
    r = reader(c, delimiter=";")
    R = [row for row in r]
    x = R[randint(0, 7)][randint(0, 3)]
X = []
n = 0
l = len(x)
for i in range(l):
    X.append(x[n])
    n += 1
Y = []
for i in range(l):
    Y.append('_')
print(Y)
points = 11
T = []
plt.figure()
ax = plt.subplot()
circle = plt.Circle((4, 7.5), 0.5, color='b')
while True:
    if points == 10:
        ax.plot([0, 2], [0, 1], 'b')
    if points == 9:
        ax.plot([2, 4], [1, 0], 'b')
    if points == 8:
        ax.plot([2, 2], [1, 10], 'b')
    if points == 7:
        ax.plot([2, 4], [10, 10], 'b')
    if points == 6:
        ax.plot([4, 4], [10, 8], 'b')
    if points == 5:
        ax.add_artist(circle)
    if points == 4:
        ax.plot([4, 4], [7, 3], 'b')
    if points == 3:
        ax.plot([3, 4], [6, 5], 'b')
    if points == 2:
        ax.plot([4, 5], [5, 6], 'b')
    if points == 1:
        ax.plot([3, 4], [2, 3], 'b')
    if Y == X:
        print("wygrałeś")
        break
    if points == 0:
        ax.plot([4, 5], [3, 2], 'b')
        print("przegrałeś")
        print(f"x to '{x}'")
        break
    a = input("podaj literę ")
    while a in T:
        print("tego już próbowałeś")
        a = input('jakiś inny pomysł ?')
    T.append(a)
    c = 0
    if a not in X:
        points -= 1
        print(f"masz jeszcze {points} prób")
    else:
        for l in X:
            if l == a:
                Y[c] = a
            c += 1
    print(Y)
    plt.show(block=False)
