def dev(i):
    d = set()
    for j in range(1, int(i**0.5) +1):
        if i%j == 0:
            if all(j%x != 0 for x in range(2, int(j**0.5) +1)):
                d.add(j)
            if all((i//j)%x != 0 for x in range(2, int((i//j)**0.5) +1)):
                d.add((i//j))
    return sorted(d)

f = open("27-2B.txt")
n, k, d = map(int, f.readline().split())
md = -10**20
a = [int(x) for x in f]
m = {x: a.count(x) for x in sorted(set(a))}
print(m, k, d)

a = sorted(a)[::-1]

p = 1
for i in range(k - 1):
    p *= a[i]
if (p * a[k - 1]) % d == 0: p = p * a[k - 1]
else:
    cp = p
    s = [x for x in dev(d)]
    for i in range(len(s)):
        if cp % s[i] != 0:
            n = 0
            #print(s[i])
        else:
            cp = cp // s[i]
            #print("were", s[i])
#print(p, '\n', sum(int(x) for x in str(p)))
