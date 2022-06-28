from itertools import *
count = 0

for x in product("1234567890", repeat = 5):
    s = ''.join(x)
    v = int(s)
    if 10000 <= v < 100000:
        c = ''
        while v > 0:
            c = str(v%9) + c
            v = v//9
        if c.count("0") == 1 and (not(any(("0" + k) in c for k in "13579"))) and\
           (not(any((j + "0") in c for j in "13579"))):
            count += 1
print(count)
