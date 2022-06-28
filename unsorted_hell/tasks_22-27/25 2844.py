def f(n):
    d = set()
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            d.add(i)
            d.add(n//i)
        if len(d) > 3:
            return 0
    sorted(d)
    if len(d) == 3:
        return max(d)
    else:
        return 0

for n in range(152346, 957813):
    a = f(n)
    if a != 0:
        print(n, a)
