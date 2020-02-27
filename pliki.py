with open('some.txt', 'r+') as p:
    print(p.read())
    p.write(input('write...'))
    print(p.read())
    p.close()
