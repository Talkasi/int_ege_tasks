f = open('27B (13).txt')
n = int(f.readline())
m = [ [] for i in range(11) ]
for i in range(n):
    x = int(f.readline())
    ost = x%11
    m[ost] += [x]

a = []
for i in range(11):
    m[i].sort()
    a += m[i][:3]

ans = []
for i in range(len(a)):
    for j in range(i + 1, len(a)):
        for k in range(j + 1, len(a)):
            if (a[i] + a[j] +a[k])%11 == 0:
                ans.append(a[i]+a[j]+a[k])
print(min(ans))
