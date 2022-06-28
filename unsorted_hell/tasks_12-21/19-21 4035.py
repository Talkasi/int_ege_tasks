from functools import *
# 19: 30 / 11
# 20: 3
# 21: 30
def m(h):
    a, b = h
    return (a * 3, b), (a, b*3), (a+1, b), (a, b+1)
@lru_cache(None)
def g(h):
    if sum(h) >= 99: return 'w'
    if any(g(x)=='w' for x in m(h)): return 'p1'
    if any(g(x)=='p1' for x in m(h)): return 'v1'
    if any(g(x)=='v1' for x in m(h)): return 'p2'
    if all(g(x)=='p1' or g(x)=='p2' for x in m(h)): return 'v2'

for i in range(1, 91):
    h = 8, i
    if g(h)=='v1':
        print(i, g(h))
