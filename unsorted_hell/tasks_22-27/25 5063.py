def p(n):
    return all(n%x != 0 for x in range(2, int(n**0.5) + 1))

def check(n):
    d = set()
    st, st1, st2 = 0, 0, 0
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            if p(i):
                d.add(i)
            if p(n//i):
                d.add(n//i)

    if len(d) == 0: return ("-1", 0)
    k = ''
    for x in sorted(d):
        k += str(x)
    #print(n, k)
    return k , max(d)
    
m = 0
for i in range(4679001, 10000000):
    a, b = check(i)
    #print(a, b)
    if len(a)>4:
        if (a[-1] == '7' and a[-3] == '2' and a[0] == '3' and a[1] == '4') or \
           (a[-2] == '9' and a[-3] == '3' and a[0] == '2' and a[1] == '7'):
            print(i, b)
            m += 1
    if i % 1000_000 == 0: print(i)
    if m == 5: break
