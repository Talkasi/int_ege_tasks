f = open("27A (18).txt")
n = int(f.readline())
m = [[] for i in range(80)]
for i in range(n):
    x = int(f.readline())
    m[x%80] += [x]
ma = 0
for i in range(80):
    m[i].sort()
    if len(m[i]) > 1:
        ma = max(ma, m[i][-1] - m[i][0])

print(ma)
