import random
print("zgadnij int'a")
x=random.randint(0, 10)
y=int(input("szczelaj"))
while y != x:
    if y == x:
        print("wygrałeś")
        break
    elif y < x:
        print("więcej")
        y = int(input("szczelaj jeszcze raz"))
    else:
        print("mniej")
        y=int(input("szczelaj jeszcze raz"))
print("end")