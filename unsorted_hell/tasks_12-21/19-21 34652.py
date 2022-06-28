from functools import *
def m(h):
    a, b = h
    if a > 1 and b > 1: return ((a+1)//2, b), (a, (b+1)//2), (a - 1, b), (a, b - 1)
    if a > 1 and b == 1: return ((a+1)//2, b), (a - 1, b), (a, b - 1)
    if a == 1 and b > 1: return (a, (b+1)//2), (a - 1, b), (a, b - 1)
    if a == 1 and b == 1: return (a - 1, b), (a, b - 1)


@lru_cache(None)
def g(h):
    a, b = h
    #if b < 0 or a < 0: return ''
    if 0 <= sum(h) <= 30: return 'w'
    if any(g(x)=='w' for x in m(h)): return 'p1'
    if all(g(x)=='p1' for x in m(h)): return 'v1'
    if any(g(x)=='v1' for x in m(h)): return 'p2'
    if all(g(x)=='p1' or g(x) == 'p2' for x in m(h)): return 'v2'
    return'n'

for s in range(13, 90):
    h = 18, s
    if g(h) == 'p2': print(g(h), s)
    
