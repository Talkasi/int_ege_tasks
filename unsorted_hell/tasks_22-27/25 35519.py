def f(n):
    d = set()
    for i in range(2, int(n**0.5) + 1):
        if n%i == 0:
            d.add(i)
            d.add(n//i)
        if len(d) > 3:
            return d
    return d

for i in range(4234679, 10157813):
    if i % int(i ** 0.5) == 0:
        a = [x for x in sorted(f(i))]
        if len(a) == 3:
            print(i, a[-1])
