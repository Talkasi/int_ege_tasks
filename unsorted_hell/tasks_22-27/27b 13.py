f = open("27A (16).txt")
n = int(f.readline())
ost = [[] for i in range(11)]
for i in range(n):
    x = int(f.readline())
    ost[x%11] += [x]
m = []
for i in range(11):
    ost[i].sort()
    m += [ost[i][0]] + [ost[i][1]] + [ost[i][2]]

a = 10**1000
for i in range(len(m)):
    for j in range(i+1, len(m)):
        for l in range(j+1, len(m)):
            if (m[i] + m[j] + m[l])%11 == 0:
                a = min(a, m[i] + m[j] + m[l])
print(a)
