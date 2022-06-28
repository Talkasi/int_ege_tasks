f = open("27_B (8).txt")
n = int(f.readline())
a = [int(x) for x in f]
m = 10**20
for j in range(n):
    s = 0
    for i in range(len(a)):
        if i > n//2: s += 3*(n - i)*a[i]
        else: s += 3*i*a[i]
    m = min(m, s)
    a = a[1:] + [a[0]]
print(m)
