from itertools import *
c, k = 0, 0

for x in product("АЕПСТУХ", repeat = 4):
    s = ''.join(x)
    c += 1
    if c > 1000 and all((not(i+i in s)) for i in "СТЕПУХА"):
        k+=1
        
print(k)
