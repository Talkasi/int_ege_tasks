def f(n):
    d = set()
    for i in range(2, int(n**0.5 + 1)):
        if n%i == 0:
            d.add(i)
            d.add(n//i)
    if len(d) > 2:
        return d
    return 0
c = 0
for i in range(10_000_001, 100000000000):
    a = f(i)
    if a != 0:
        a = sorted([x for x in f(i)])
        s = a[-1] + a[-2] + a[-3]
        if all( s%h != 0 for h in range(2, int(s**0.5 + 1))):
            print(s)
            c+=1
        if c == 5:
            break
