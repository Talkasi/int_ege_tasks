f = open("27B (5).txt")
n = int(f.readline())
a = [0]*131

for i in range(n):
    x = int(f.readline())
    ost = x%131
    a[ost] += 1

ans = a[0]*(a[0] - 1)//2
for i in range(1, 131//2+1):
    ans += a[i]*a[131 - i]
print(ans)
