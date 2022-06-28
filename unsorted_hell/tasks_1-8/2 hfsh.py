k = 0,1
for x in k:
    for y in k:
        for z in k:
            if not((x <= z) and not(x and y and z)):
                print(x, y, z)

def f(n, k, c):
    if n > k: return 0
    if n == k and c == 1: return 1
    if n == k and c == 0: return 0
    return f(n + 1, k, 1) + f(n + 2, k, 0)
print('#23', f(4, 13, 0) + f(4, 12, 0))

s = open('24-157.txt').readline()
c, m = '', ''
for i in range(len(s)):
    c += s[i]
    while 'QW' in c: c = c[1:]
    m = max(m, c, key = len)
print('#24a', len(m))

s = s.replace('QW', '*').split('*')
m = max([x for x in s], key = len)
if m == s[0] or m == s[-1]: m = m + 'Q'
else: m = m + 'QQ'
print('#24b', len(m))

def g(n):
    d = set()
    for i in range(1, int(n**0.5) + 1):
        if n%i == 0:
            d.add(i)
            d.add(n//i)
    return sum(d)

ans = []
for i in range(2, 263001):
    if g(g(i)) == i * 2:
        ans.append(i)
print('#25', len(ans), max(ans))

for i in range(10, 100):
    for j in range(10, 100):
        if i - j == 14 and any(x in str(j) for x in str(i)): print(i, j)
