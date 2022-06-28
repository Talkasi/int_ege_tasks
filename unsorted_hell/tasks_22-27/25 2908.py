def f(n):
    d = set()
    for i in range(2,int(n**0.5 + 1)):
        if n%i == 0:
            d.add(i)
            d.add(n//i)
    if d!=set():
        return (len(d), max(d))
    return 0

m = 0
for n in range(586132, 586431):
    a = f(n)
    if a != 0:
        m = max(m, a[0])

for n in range(586132, 586431):
    a = f(n)
    if a != 0 and a[0] == m:
        n, j = a
        print(n+2, j)
    
