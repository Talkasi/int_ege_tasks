f = open("27-98a.txt")
n, k = map(int, f.readline().split())
l = set()
m, le = 10**20, 0
stat = [ 0 ] * k

for i in range(n):
    x = int(f.readline())
    le += 1
    l.add(x)
    if len(l) == k: m = min(m, le)
    if len(l) >= k: m = min(m, le - stat[len(l) - k])

    stat[ len(l) - 1 ] = max(stat[ len(l) - 1], le)
print(m)
