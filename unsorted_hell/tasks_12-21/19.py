from functools import *
def m(h):
    a, b = h
    return (a+b, b), (a, a+b), (a, b+1), (a+1, b)
@lru_cache(None)
def g(h):
    if sum(h) >= 79: return 'w'
    if any(g(x) == 'w' for x in m(h)): return 'p1'
    if all(g(x) == 'p1' for x in m(h)): return 'v1'
    if any(g(x) == 'v1' for x in m(h)): return 'p2'
    if all(g(x) == 'p1' or g(x) == 'p2' for x in m(h)): return 'v2'

for i in range(1, 70):
    if g((9, i)) == 'v2': print( g((9, i)), i)
