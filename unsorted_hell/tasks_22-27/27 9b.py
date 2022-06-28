f = open('27 test.txt')
n = int(f.readline())
m = [0]*2001
c = 0
for i in range(n):
    x = int(f.readline())
    if x <= 2000: m[x] += 1
ans = m[1000]*(m[1000] - 1)//2
for i in range(1000):
    ans += m[i]*m[2000 - i]
print(ans)
