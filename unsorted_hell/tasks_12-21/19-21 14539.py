from functools import *
def m(h):
    a, b = h
    return (a, b*2), (a*2, b), (a+3, b), (a, b+3)
@lru_cache(None)
def g(h):

    if sum(h) >= 62: return 'w'
    if any(g(x)=='w' for x in m(h)): return 'p1'
    if all(g(x)=='p1' for x in m(h)): return 'v1'
    if any(g(x)=='v1' for x in m(h)): return 'p2'
    if all(g(x)=='p1' or g(x) == 'p2' for x in m(h)): return 'v2'

for i in range(1, 55):
    h = 7, i
    if g(h) == 'v2': print(g(h), i)

for i in range(1, 100000):
    s = i
    n = -5
    while s > 10:
        s = s - 8
        n = n + 3
    if n == 67:
        print(i)

