def f(n):
    return all(n%x!= 0 for x in range(2, int(n ** 0.5) + 1))
c = 0
for i in range(4671032, 4671107):
    if f(i):
        c += 1
        print(c, i)
