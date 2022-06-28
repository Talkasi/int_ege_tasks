def f(n):
    d = set()
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            d.add(i)
            d.add(n//i)
    return sum(d) + 1
print(220, f(220), 284, f(284))

for i in range(2, 30001):
    a = f(i)
    b = f(f(i))
    if i == b and b < a:
        print(b, a)
