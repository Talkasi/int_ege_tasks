f = open("27-1B.txt")
n, k, d = map(int, f.readline().split())
colv, k0 = 0, 0
stat = [[0]*(d) for i in range(k)]

for i in range(n):
    x = int(f.readline())

    if x == 0: k0 += 1
    else: colv += stat[k0 % k][d - x%d if x%d != 0 else 0]

    #stat
    if x != 0:
        stat[k0 % k][x % d] += 1
print(colv)
