class Place:
    def __init__(self, x, y, function):
        self.coordinates = (x, y)
        self.function = function
        if self.function == 'f':
            self.value = 0
        elif self.function == 'w':
            self.value = '#'
        else:
            self.value = 'none'


def stop(li):
    st = 0
    for s in li:
        if s.value == 'none':
            st += 1
    return st


Lt = [Place(0, 0, 'w'), Place(1, 0, 'f'), Place(2, 0, 'w'), Place(0, 1, 'w'), Place(1, 1, 'n'), Place(2, 1, 'w'), Place(0, 2, 'w'), Place(1, 2, 's'), Place(2, 2, 'w')]
n = []
p = 0
for i in Lt:
    if i.function == 'f':
        n.append(i.coordinates)
        break
for q in n:
    stopper = stop(Lt)
    if stopper == 0:
        break
    for a in Lt:
        if a.coordinates[0] == q[0]+1 and a.coordinates[1] == q[1]:
            n.append(a.coordinates)
            a.value = p+1
        elif a.coordinates[0] == q[0]-1 and a.coordinates[1] == q[1]:
            n.append(a.coordinates)
            a.value = p+1
        elif a.coordinates[0] == q[0] and a.coordinates[1] == q[1]+1:
            n.append(a.coordinates)
            a.value = p+1
        elif a.coordinates[0] == q[0] and a.coordinates[1] == q[1]-1:
            n.append(a.coordinates)
            a.value = p+1
    n.remove(q)
Exit = []
for e in Lt:
    r = e.value
    Exit.append(r)
    Lt.remove(e)
print(Exit)