def f(n):
    d = set()
    for i in range(2, n//2+1):
        if n%i == 0:
            d.add(i)
    return sum(d)

k = 0
for i in range(150001, 10000000000):
    if f(i)%13 == 10:
        k += 1
        print(i, f(i))
    if k == 7:
        break
