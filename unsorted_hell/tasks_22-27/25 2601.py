def p(i):
    return all(i%j!=0 for j in range(2, int(i**0.5) + 1))

def f(n):
    d = set()
    for i in range(2, int(n**0.5) + 1):
        if n%i == 0 and p(i):
            d.add(i)
            d.add(n//i)
    return d

s, c = 0, 0
for n in range(351627, 428764):
    a = [i for i in f(n) if p(i)]
    if len(a) == 2:
        d, b = a
        if d * b == n:
            c += 1
            s += n
print(c, s//c)
