def f(n):
    d = set()
    for i in range(2, int(n**0.5) + 1):
        if n%i == 0:
            d.add(i)
            d.add(n//i)
        if len(d) > 4:
            return 0
    if len(d) == 4:
        return d
    return 0

for i in range(157898, 157991):
    a = f(i)
    if a != 0:
        d = [x for x in a]
        d.sort()
        print(d[-1], d[-2])
