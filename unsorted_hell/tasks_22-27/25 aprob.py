def f(n):
    d = set()
    for i in range(2, int(n ** 0.5) + 1):
        if n%i == 0:
            d.add(n//i)
            d.add(i)
    return sorted(d)
k = 0
for n in range(220_000, 500_000):
    a = [x for x in f(n)]
    if len(a) > 1 and (a[0] + a[-1]) % 10 == 4:
        print(n, a[0] + a[-1])
        k += 1
    if k == 5: break
