f = open("27B (41).txt")
n = int(f.readline())
q = [int(f.readline()) for i in range(5)]
c = 0
# ch - nch
ost = [[0]*13 for i in range(2)]

for i in range(n - 5):
    x = int(f.readline())
    if x%2 == 0: c += ost[0][x%13] + ost[1][x%13]
    if x%2 != 0: c += ost[0][x%13]

    ost[q[0]%2][q[0]%13] += 1
    q.append(x)
    q.pop(0)
print(c)
    
