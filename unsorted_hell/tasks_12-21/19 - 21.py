from functools import *

def m(h):
    a, b = h
    return (a * 2, b), (a, b * 2), (a + 1, b), (a, b + 1)

@lru_cache(None)
def g(h):
    if sum(h) >= 211: return 'w'
    if any(g(x) == 'w' for x in m(h)): return 'p1'
    if any(g(x) == 'p1' for x in m(h)): return 'v1'
    if any(g(x) == 'v1' for x in m(h)): return 'p2'
    if all(g(x) == 'p1' or g(x) == 'p2' for x in m(h)): return 'v2'

for s in range(1, 194):
    h = 17, s
    if g(h) == 'v1': print(g(h), s)
