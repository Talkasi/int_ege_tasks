from functools import *

def m(n):
    a, b = n
    return (a*2, b), (a, b*2), (a + 1, b), (a, b + 1)

@lru_cache(None)
def g(h):
    if sum(h) > 86: return 'w'
    if any(g(n) == 'w' for n in m(h)): return 'p1'
    if any(g(n) == 'p1' for n in m(h)): return 'v1'
    if any(g(n) == 'v1' for n in m(h)): return 'p2'
    if all(g(n) == 'p1' or g(n) == 'p2' for n in m(h)): return 'v2'
    return ""

for s in range(1, 78):
    h = 9, s
    if g(h) == 'v1':
        print(g(h), s)
    
