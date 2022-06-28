f = open("27-87a.txt")
n, k = map(int, f.readline().split())
s, os, m, st = 0, 0, -10**10, 0
stat = [10**20] * k
for i in range(n):
    x = int(f.readline())
    s += x

    if x < 0:
        st = 0
        copy = abs(x)
        while copy > 0:
            if copy % 5 == 2:
                st = 1
                break
            copy = copy // 5
        if not (st): os += 1

    if os % k == 0: m = max(m, s)
    m = max(m, s - stat[ os % k ])

    stat[ os % k ] = min(stat[ os % k ], s)
print(m, stat)
    
