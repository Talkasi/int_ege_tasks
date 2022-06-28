def f(n):
    d = set()
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            d.add(i)
            d.add(n//i)
    return len(d)
m = 0
for i in range(394441, 394506):
    a = f(i)
    if a > m:
        m = a
        c = i
print(m + 2, c)
