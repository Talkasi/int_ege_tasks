k = 0, 1
for x in k:
    for y in k:
        for z in k:
            print(x, y, z, ((x <= y) and (y <= z)))

for i in range(10, 100):
    for j in range(10, 100):
        if i - j == 50 and len(set(str(i)+str(j))) <= 3:
            #print(i, j)
            l = 0

from itertools import *
c = 0
for i in product('AI', repeat = 2):
    s = ''.join(i)
    if s.count('A') <= 2 and s.count('I') <= 2: c+=1
print(c)
