def f(n):
    d = set()
    for i in range(1, int(n**0.5) + 1):
        if n%i == 0:
            d.add(i)
            d.add(n//i)
    return sorted(d)
c = 0
for i in range(125_873, 136_763):
    a = [x for x in f(i)]
    if len(a) == 5:
        c += 1
        m = i
print(c, m)
