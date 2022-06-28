from itertools import *
c = 0
for i in permutations('VAIFY', r = 4):
    s = ''.join(i)
    if s[0]!='I' and not('VF' in s) and not('FV' in s):
        c+=1
print(c)
