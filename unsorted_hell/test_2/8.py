from itertools import *
c, k = 0, 0
for x in permutations('KLABXAYS', r = 8):
    s = ''.join(x)
    for i in range(len(s) - 1):
        if s[i] == s[i+1]:
            c = 1
            break
    if c == 0:
        k += 1
    c = 0
print(k / 2)
