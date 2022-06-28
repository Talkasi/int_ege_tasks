def f(n):
    d = set()
    for i in range(2,int(n ** 0.5) + 1):
        if n%i == 0:
            d.add(i)
            d.add(n//i)
    if len(d) < 5:
        return 0, 0
    return pr(sorted(d))

def pr(d):
    s = 1
    l = 0
    for i in d:
        s *= int(i)
        l += 1
        m = int(i)
        if l == 5:
            break
    return s, m

c = 0
for x in range(400000001, 1000000000):
    a, b = f(x)
    if a%100 == 17 and a <= x:
        print(a, b, )
        c += 1
    if c == 5:
        break

