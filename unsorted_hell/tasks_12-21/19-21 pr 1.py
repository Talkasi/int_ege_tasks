from functools import *

def m(h):
    a, b = h
    return (a*2, b), (a, b*2), (a, b+1), (a+1, b)

@lru_cache(None)
def g(h):
    if sum(h) > 230: return 'w'
    if any(g(x)=='w' for x in m(h)): return 'p1'
    if all(g(x)=='p1' for x in m(h)): return 'v1'
    if any(g(x)=='v1' for x in m(h)): return 'p2'
    if all(g(x)=='p1' or g(x)=='p2' for x in m(h)): return 'v2'

for j in range(1, 214):
    h = 17, j
    if g(h) == 'v2': print(g(h), j)
