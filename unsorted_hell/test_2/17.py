f = open('17-4 (1).txt')
a = []
ans = []
for i in f:
    a.append(int(i))
sr = sum(a)/len(a)
for i in range(len(a) - 1):
    if a[i] > sr or a[i + 1] > sr and (a[i] + a[j])%7 == 0:
        ans.append(a[i] + a[j])
print(len(ans), max(ans))
