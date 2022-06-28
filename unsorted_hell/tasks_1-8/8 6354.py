'''
from itertools import *
c = 0
for i in permutations('ЕСАУЛ', r = 5):
    s = ''.join(i)
    if not(any(x+y in s for x in 'ЕАУ' for y in 'ЕАУ')):
        c += 1
print(c)


def f(n):
    print(n - 5, n)
    if n > 1:
        print(n + 8, n)
        f(n - 2)
        f(n - 3)

f(5)
'''
from functools import *
@lru_cache(None)
def f(n):
    su = n - 5
    if n > 1:
        su += n + 8 + f(n - 2) + f(n - 3)
    return su

for i in range(1, 300):
    a = f(i)
    if a > 3200000:
        print(i, a)
        break
