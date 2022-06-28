def f(n):
    d = set()
    for i in range(2, int(n**0.5) + 1):
        if n%i == 0:
            d.add(i)
            d.add(n//i)
    if len(d) == 4:
        return max(d)
    else:
        return 0

for m in range(164700, 164753):
    a = f(m)
    if a != 0:
        print(a, m)
