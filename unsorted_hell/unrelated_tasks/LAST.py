#17
a = [int(x) for x in open("17 (13).txt")]
ma = max(x for x in a if x % 11 == 0)
ans = []

for i in range(len(a) - 1):
    if (a[i] > ma or a[i+1] > ma):
        ans.append(a[i] + a[i+1])
print(len(ans), min(ans))

#19-21
from functools import *

def m(h):
    a, b = h
    return (a*2, b), (a, b*2), (a+3, b), (a, b+3)

@lru_cache(None)
def g(h):
    if sum(h) >= 300: return 'w'
    if any(g(x) == 'w' for x in m(h)): return 'p1'
    if all(g(x) == 'p1' for x in m(h)): return 'v1'

    if any(g(x) == 'v1' for x in m(h)): return 'p2'
    if all(g(x) == 'p2' or g(x) == 'p1' for x in m(h)): return 'v2'

    if any(g(x) == 'v1' or g(x) == 'v2' for x in m(h)): return 'p3'

for s in range(1, 280):
    h = 20, s
    if g(h) == 'p3': print(g(h), s)


































