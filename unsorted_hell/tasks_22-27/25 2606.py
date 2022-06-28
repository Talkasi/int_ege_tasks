def f(n):
    d = set()
    for i in range(2, int(n**0.5) +1):
        if n%i == 0:
            d.add(i)
            d.add(n//i)
    return sorted(d)

def g(n):
    return not any(n % i == 0 for i in range(2, int(n**0.5) + 1))

c = 0
r = 0
for i in range(238941, 315676):
    a = [x for x in f(i) if g(x)]
    if len(a) == 2 and a[0] * a[1] == i:
        c += 1
        if a[1] - a[0] > r:
            r = a[1] - a[0]
            m = i
print(c, m)
