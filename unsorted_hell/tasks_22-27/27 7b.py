f = open("27A (6).txt")
#3 23
#разность остатков равна 0

n = int(f.readline())
a = [0]*69

for i in range(n):
    x = int(f.readline())
    a[x%69] += 1

ans = 0
for i in range(69):
    ans += a[i]*(a[i]-1)//2
print(ans)
