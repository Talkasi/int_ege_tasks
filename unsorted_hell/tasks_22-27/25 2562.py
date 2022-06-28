def f(n):
    d = set()
    for i in range(2, int(n**0.5)+1):
        if n%i == 0:
            d.add(i)
            d.add(n//i)
        if len(d)>2:
            return 0
    if len(d) == 2:
        return sorted(d)
    return 0

for n in range(174457, 174506):
    a = f(n)
    if a!= 0:
        b, c = a
        print(b, c)
    
