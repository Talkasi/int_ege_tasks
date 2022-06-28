def f(n):
    return all( n%i !=0 for i in range(2, int(n**0.5)+1))

for x in range(55_000_000, 60_000_001):
    t = x
    while t%2==0: t = t//2
    if int(t**0.25)**4 == t and f(int(t**0.25)):
        print(x, t)
        
