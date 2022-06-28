from itertools import *
c = 0
for x in product("АБРТЫ", repeat = 5):
    s = ''.join(x)
    c+=1
    if s.count("Ы") == 0 and (not("АА" in s)):
        print(c)
        print(s)
        break
