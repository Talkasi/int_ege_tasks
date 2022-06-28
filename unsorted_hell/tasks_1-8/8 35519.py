from itertools import *
c = 0
for x in product('SLON', repeat = 5):
    s = ''.join(x)
    if s.count('S') == 1:
        c+=1
print(c)
