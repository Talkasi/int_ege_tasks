f = open('27-81a.txt')
n = int(f.readline())
kn, m, s = 0, 0, 0
stat = [10**20] * 13
for i in range(n):
    x = int(f.readline())
    s += x
    if x % 2 == 1: kn += 1
    #Special case
    if kn % 13 == 0: m = max(m, s)

    m = max(m, s - stat[ kn%13 ])

    #stat
    stat[ kn%13 ] = min(stat[ kn%13 ], s)
print(m)
