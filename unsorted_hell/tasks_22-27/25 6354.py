def f(n):
    d = set()
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            d.add(i)
            d.add(n//i)
    return sorted(d)

for i in range(174_457, 174_506):
    a = [x for x in f(i)]
    if len(a) == 2:
        print(a[0], a[1])
        if a[0]*a[1] != i: print('error')
