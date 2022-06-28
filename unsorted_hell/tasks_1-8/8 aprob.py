from itertools import *
c = 0
for x in product("0123456", repeat = 7):
    s = ''.join(x)
    if s[0] != '0' and s[0]!='3' and s[0]!='5' and not ('22' in s and '44' in s):
        c+=1
print(c)
