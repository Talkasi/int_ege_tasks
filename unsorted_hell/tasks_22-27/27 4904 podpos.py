f = open("27-96a.txt")
n = int(f.readline())
s, k7, k5 = 0, 0, 0
statsum = [[10**20]*7 for i in range(5)]
ms = 0
for i in range(n):
    x = int(f.readline())
    s += x
    if x%5 == 0: k5 += 1
    if x%7 == 0: k7 += 1
    #Special case
    if k5 == k7: ms = max(ms, s)
    ms = max(ms, s - statsum[k5%5][k7%7])
    a = 4 - k5%5
    b = 6 - k7%7
    statsum[k5%5][k7%7] = min(statsum[a][b], s)
print(ms)
