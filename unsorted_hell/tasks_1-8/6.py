#17
a = [int(x) for x in open("17-4 (3).txt")]
ans = []

for i in range(len(a)):
    if len(bin(a[i])[2:]) >3 and (bin(a[i])[2:])[-4:] == '1001':
        s = a[i]
        d = ''
        while s > 0:
            d = str(s % 5) + d
            s = s//5
        if d[-2:] == '11':
            ans.append(a[i])
print(max(ans), sum(ans))

#19-21
from functools import *

def m(h):
    a, b = h
    return (a*2, b), (a, b * 2), (a+1, b), (a, b+1)

@lru_cache(None)
def g(h):
    if sum(h) >= 53: return 'w'
    if any(g(x) == 'w' for x in m(h)): return 'p1'
    if all(g(x) == 'p1' for x in m(h)): return 'v1'
    if any(g(x) == 'v1' for x in m(h)): return 'p2'
    if all(g(x) == 'p1' or g(x) == 'p2' for x in m(h)): return 'v2'

for i in range(1, 44):
    h = 9, i
    if g(h) == 'v2': print(g(h), i)

#22
for i in range(1000, 10000):
    n = i
    a = -1
    while n > 9 and a != n % 10:
        a = n % 10
        n = n //10
    if n % 10 == 4:
        print(i)
        break

#23
def f(n, k):
    if n == k: return 1
    if n > k: return 0
    j = int(''.join(str(int(x) + int(x != '9')) for x in str(n)))
    return f(n+1, k) + f(j, k)
print(f(26, 49))

#24
m = 0
'''24-164 (1)'''
for s in open("24-164 (1).txt"):
    if s.count('E') < 20:
        for i in set(s):
            m = max(m, s.rfind(i) - s.find(i))
print(m)

#25
def f(n):
    d = set()
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            d.add(i)
            d.add(n//i)
    return len(d)

m = 0
for i in range(394441, 394506):
    a = f(i)
    if a > m:
        m = a
        k = i
print(m, k)

#27 "27-50a.txt"
f = open("jk.txt")
n = int(f.readline())
s = [[0,0,0]]
for i in range(n):
    p = [int(x) for x in f.readline().split()]
    s = [[a[0] + b, a[1] + (b%2 == 0), a[2] + (b%2 == 1)] for a in s for b in p]
    s = {(a[0]%2, (1 if a[2] > a[1] else 0)):a for a in sorted(s)}
    if i != n - 1: s = s.values()
print(max(s[(0, 1)][0] if (0, 1) in s else 0, s[(1, 0)][0] if (1, 0) in s else 0))
    
#16
def f(n):
    if n == 1: return 1
    if n >= 2: return f(n - 1) + 3 * g(n - 1)

def g(n):
    if n == 1: return 1
    if n >= 2: return f(n - 1) - 2 * g(n - 1)

print(sum(int(x) for x in str(f(18))))

#15
for a in range(1, 100000):
    if all((2*y+x < a) or (x>10) or (y>25) for x in range(1, 100) for y in range(1, 100)):
        print(a)
        break

#14
s = 9**8 + 3 ** 5 - 9
c = 0
while s > 0:
    if s % 3 == 2: c+=1
    s = s//3
print(c)

#12
for i in range(36, 1000):
    s = '1'*i
    while '111' in s:
        s = s.replace('111', '2', 1)
        s = s.replace('222', '1', 1)
    if s == '1':
        print(i)
        break

#23
def f(n,c):
    if n==c: return 1
    if n>c: return 0
    if n<c and n%10!=9: return f(n+1,c)+ f((n+int('1'*len(str(n)))),c)
    else: return f(n+1,c)+ f((n-1+int('1'*len(str(n)))),c)
print(f(26,49))

    













        
