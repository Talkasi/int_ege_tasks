from itertools import *
c = 0
for x in product("АБКЛУ", repeat = 4):
    s = ''.join(x)
    c+=1
    if len(set(s)) == 4:
        k = s
        kn = c
    if s == 'УЛКБ':
        print(c)
print(k, kn)
