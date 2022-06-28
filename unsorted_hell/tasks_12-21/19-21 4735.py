from functools import *
# 3
# 2 30
# 14
def m(h):
    a, b = h
    return (a*2, b), (a, b*2), (a+2, b), (a, b+2)
@lru_cache(None)
def g(h):
    if sum(h) > 74: return 'p1'
    if sum(h) >= 63: return 'w'
    if any(g(x)=='w' for x in m(h)): return 'p1'
    if any(g(x)=='p1' for x in m(h)): return 'v1'
    if any(g(x)=='v1' for x in m(h)): return 'p2'
    if all(g(x)=='p1' or g(x)=='p2' for x in m(h)): return 'v2'

for i in range(1, 48):
    h = 15, i
    if g(h)=='v1':
        print(i, g(h))
