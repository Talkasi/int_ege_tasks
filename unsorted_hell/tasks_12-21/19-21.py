from functools import *
def m(h):
    a, b = h
    return (a+1, b), (a, b+1), (a +b, b), (a, b + a)

@lru_cache(None)
def g(h):
    a, b = h
    if sum(h) >= 73: return 'w'
    if any(g(x)=='w' for x in m(h)): return 'p1'
    if all(g(x)=='p1' for x in m(h)): return 'v1'
    if any(g(x)=='v1' for x in m(h)): return 'p2'
    if all(g(x)=='p1' or g(x) == 'p2' for x in m(h)): return 'v2'

for s in range(1, 64):
    h = 9, s
    if g(h) == 'v2': print(g(h), s)
    
