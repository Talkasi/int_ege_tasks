from functools import *

def m(h):
    return h + 1, h + 2, h * 2

@lru_cache(None)
def g(h):
    if h >= 22: return 'w'
    if any(g(x) == 'w' for x in m(h)): return 'p1'
    if all(g(x) == 'p1' for x in m(h)): return 'v1'
    if any(g(x) == 'v1' for x in m(h)): return 'p2'
    if all(g(x) == 'p1' or g(x) == 'p2' for x in m(h)): return 'v2'
    if any(g(x) == 'v1' or g(x) == 'v2' for x in m(h)): return 'p3'
    if all(g(x) == 'p1' or g(x) == 'p2' or g(x) == 'p3' for x in m(h)): return 'v3'
    if any(g(x) == 'v1' or g(x) == 'v2' or g(x) == 'v3' for x in m(h)): return 'p4'
    if all(g(x) == 'p1' or g(x) == 'p2' or g(x) == 'p3' or g(x) == 'p4' for x in m(h)): return 'v4'
k = 0
for i in range(1, 22):
    if g(i) == 'v1' or g(i) == 'v2' or g(i) == 'v3' or g(i) == 'v4':
        k += 1
        print(i, g(i))
print(k)
