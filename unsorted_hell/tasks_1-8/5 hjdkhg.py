
'''
for i in range(1001, 100000):
    n = bin(i)[2:]
    n = n[::-1]
    while n[0] == '0': n = n[1:]
    n = int(n, 2)
    if n == 29:
        print(i)
        break
for i in range(1, 100000):
    d = i
    n = 2
    s = 0
    while s <= 365:
        s = s+d
        n = n+5
    if n == 67:
        print(i)
        break





s = "3" + "5" *57

while '25' in s or '355' in s or '4555' in s:
    if '25' in s: s = s.replace("25", "3", 1)
    if '355' in s: s = s.replace("355", "4", 1)
    if "4555" in s: s = s.replace("4555", "2", 1)
print(s)


c = 0
s = 81**15 + 3 **22 - 27
while s > 0:
    if s % 9 == 8: c+= 1
    s = s//9
print(c)





for a in range(1, 1000000):
    if all((x&13 == 0) <= ((x&40!=0) <= (x&a != 0)) for x in range(1, 100000)):
        print(a)
        break
def f(n):
    if n< 2: return 1
    if n % 3 == 0: return f(n//3) - 1
    return f(n - 1) + 17

for i in range(1, 100000):
    if f(i) == 110:
        print(i)
        break

a = [int(x) for x in open("17-10.txt")]
ans = []

for i in range(len(a) - 1):
    if 99< (a[i] + a[i+1])<1000 and (a[i] + a[i+1])%10 > (a[i] + a[i+1])//10%10:
        ans.append(a[i] + a[i+1])
print(len(ans), min(ans))








from functools import *

def m(h):
    a, b= h
    return (a+1, b), (a, b+1), (a+b, b), (a, b+a)

@lru_cache(None)
def g(h):
    if sum(h) >= 80: return 'w'
    if any(g(x) == 'w' for x in m(h)): return 'p1'
    if all(g(x) == 'p1' for x in m(h)): return 'v1'
    if any(g(x) == 'v1' for x in m(h)): return 'p2'
    if all(g(x) == 'p1' or g(x) == 'p2' for x in m(h)): return 'v2'

for i in range(1, 72):
    h = 8, i
    if g(h) == 'v2': print(g(h), i)




def f(n, k):
    if n > k: return 0
    if n == k: return 1
    return f(n+1, k) + f(n+2, k)

print(f(1, 7) * f(7, 12))








s = open("k7a-1.txt").readline().strip()

for i in 'DE': s = s.replace(i, ' ')

s = s.split()
print(max(s, key = len), len(max(s, key = len)))







s = 0
for i in range(3159, 31584):
    if all(i%j!= 0 for j in range(2, int(i**0.5) + 1)):
        s += sum(int(x) for x in str(i))
print(s)
f = open("27-4b.txt")
n = int(f.readline())
s = [0]

for i in range(n):
    x = [int(x) for x in f.readline().split()]
    s = [a+b for a in s for b in x]
    s = {x%5:x for x in sorted(s)}.values()

print(max(x for x in s if x%5 == 0))
k = 0,1
for x in k:
    for y in k:
        for z in k:
            print(x, y, z, (not(x == (y <= z))))'''

from itertools import *
c = 0
for i in product("ЕИЯ", repeat = 2):
    s = "".join(i)
    if s.count("Е") <= 2 and s.count("И") <= 2 and s.count("Я") <= 2:
        c += 1
print(c)
































