def p(n):
    d = set()
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            d.add(i)
            d.add(n//i)
        if len(d) >=10:
            break
    if len(d) < 5: return 0, 0
    else:
        d = sorted([x for x in d])
        return (d[0]*d[1]*d[2]*d[3]*d[4], d[4])
c = 0
for i in range(500_000_001, 501_000_001):
    a, m = p(i)
    if a % 100 == 91 and a < i:
        c += 1
        print(a, m)
    if c == 5: break
