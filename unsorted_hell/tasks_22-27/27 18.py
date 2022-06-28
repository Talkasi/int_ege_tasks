f = open('27A (31).txt')
n = int(f.readline())
a = []
for i in range(n):
    x = int(f.readline())
    if x <= 134:
        a.append(x)

print(len(a))
ans = []
for i in range(len(a)):
    for j in range(i + 1, len(a)):
        if a[i] > a[j] and a[i]+a[j] <= 134:
            ans.append(a[i]+a[j])
print(len(ans), ans)
