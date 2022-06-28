def f(n, k):
    if n > k: return 0
    if n == k: return 1
    return f(n+1, k) + f(n*10+1, k)
print(f(1, 344))

from functools import *
@lru_cache(None)
def m(k):
    d = set()
    for i in range(1, int(k**0.5)+1):
        if k % i == 0:
            if i % 2 == 0: d.add(i)
            if (k//i) % 2 == 0: d.add(k//i)
    return len(d) % 2
l = 0
for k in range(1, 10000000):
    a = m(900_000_000+k)
    if a:
        print(k)
        l +=1
    if l == 5: break
