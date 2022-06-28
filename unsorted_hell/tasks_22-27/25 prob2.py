def f(n):
    d = set()
    for i in range(2, int(n **0.5) + 1):
        if n % i == 0:
            d.add(i)
            d.add(n//i)
    return sorted(d)

c = 0
for i in range(200_000_001, 4000000000000):
    a = [x for x in f(i) if x % 2 != 0]
    if len(a) > 5:
        c += 1
        print(i, a[-6])
    if c == 5: break
