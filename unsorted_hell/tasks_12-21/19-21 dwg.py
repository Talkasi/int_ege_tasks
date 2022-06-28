from functools import *
def m(h):
    a, b = h
    return (a * 4, b), (a, b * 4), (a + 1, b), (a, b + 1)

@lru_cache(None)
def g(h):
    if sum(h) >= 129: return 'w'
    if any(g(x) == 'w' for x in m(h)): return 'p1'
    if all(g(x) == 'p1' for x in m(h)): return 'v1'
    if any(g(x) == 'v1' for x in m(h)): return 'p2'
    if all(g(x) == 'p1' or g(x) == 'p2' for x in m(h)): return 'v2'

for s in range(1, 125):
    h = 4, s
    if g(h) == 'v2': print(g(h), s)
