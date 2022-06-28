from functools import *
# 7
# 4 7
# 8
def m(h):
    a, b = h
    return (a*2, b), (a, b*3), (a+1, b), (a, b+1)
@lru_cache(None)
def g(h):
    if sum(h) >= 30: return 'w'
    if any(g(x)=='w' for x in m(h)): return 'p1'
    if all(g(x)=='p1' for x in m(h)): return 'v1'
    if any(g(x)=='v1' for x in m(h)): return 'p2'
    if all(g(x)=='p1' or g(x)=='p2' for x in m(h)): return 'v2'
c = 0
for k in range(1, 30):
    if k+1 <= 29:
        h = 1, k
        if g(h) == 'v2':
            print(k)
print(c)
