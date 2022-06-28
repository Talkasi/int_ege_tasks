from functools import *

def m(a):
    return (a + 1, a + 4, a * 2)
@lru_cache(None)
def g(h):
    if h >= 40: return 'w'
    if any(g(x)=='w' for x in m(h)): return 'p1'
    if all(g(x)=='p1' for x in m(h)): return 'v1'
    if any(g(x)=='v1' for x in m(h)): return 'p2'
    if all(g(x)=='p1' or g(x) == 'p2' for x in m(h)): return 'v2'

for i in range(1, 40):
    if g(i) == 'v2': print(g(i), i)
