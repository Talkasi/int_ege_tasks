from itertools import *
f = open('27A (12).txt')
n = int(f.readline())
a = [int(x) for x in f]
m = 0
for x, y in combinations(a, 2):
    if (x+y) %2 != 0:
        m = max(m, x+y)
print(m)
