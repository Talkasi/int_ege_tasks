from functools import *
def m(h):
    a, b = h
    return (a+b, b), (a, a+b), (a+1, b), (a, b+1)

@lru_cache(None)
def g(h):
    if sum(h) >= 73: return 'w'
    if any(g(x) == 'w' for x in m(h)): return 'p1'
    if all(g(x) == 'p1' for x in m(h)): return 'v1'
    if any(g(x) == 'v1' for x in m(h)): return 'p2'
    if all(g(x) == 'p2' or g(x) == 'p1' for x in m(h)): return 'v2'

for i in range(1, 64):
    h = 9, i
    if g(h) == 'v2':
        print(g(h), i)
    
