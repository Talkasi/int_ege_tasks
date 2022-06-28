f = open("27B (17).txt")
n = int(f.readline())
m = [[] for i in range(12)]

for i in range(n):
    x = int(f.readline())
    m[x%12] += [x]
a = []
for i in range(12):
    m[i].sort()
    a += m[i][-4:]
a.sort()
ma = 0
for i in range(len(a)):
    for j in range(i+1, len(a)):
        for k in range(j+1, len(a)):
            for s in range(k+1, len(a)):
                if (a[i]*a[j]*a[k]*a[s]) %12 == 0:
                    ma = max(a[i]+a[j]+a[k]+a[s], ma)
print(ma)
