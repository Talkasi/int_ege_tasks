m = 0
k = ''
for s in open('24 (25).txt'):
    k += s.strip()
    if s.count('Q') >= m:
        m = s.count('Q')
        c = s.strip()

n = len(c)
for i in sorted(set(c)):
    if c.count(i) < n:
        n = c.count(i)
        na = i
b = {x: k.count(x) for x in sorted(set(k))}
print(na)
print(b)
