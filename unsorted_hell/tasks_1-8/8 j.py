from itertools import *

c = 0
for x in product("0123456", repeat = 7):
    s = ''.join(x)
    if all(s[0] != y for y in '035') and not(all((y+y) in s for y in "24")):
        c += 1
print(c)
