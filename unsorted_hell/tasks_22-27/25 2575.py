def f(n):
    d = set()
    for i in range(2, int(n**0.5) + 1):
        if n%i == 0:
            d.add(i)
            d.add(n//i)
        if len(d)>3:
            return 0
    d = sorted(d)
    if len(d) == 3:
        return d
    else:
        return 0

for i in range(244143, 1367822):
    a = f(i)
    if a != 0:
        x, b, c = a
        print(b, c)
