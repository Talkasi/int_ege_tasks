f = open("27B (8).txt")
n = int(f.readline())
a_mi = [0]*80
a_ma = [0]*80
a = [0]*80
c = 0
for i in range(n):
    x = int(f.readline())
    if x>50000: a_ma[x%80] += 1
    else: a_mi[x%80] += 1
    a[x%80] += 1
ans = a[0]*(a[0] - 1) // 2 + a[40]*(a[40] - 1)//2
for i in range(1, 40):
    ans += a[i]*a[80 - i]
    
b = a_mi[0]*(a_mi[0] - 1)//2 + a_mi[40]*(a_mi[40] -1)//2
for i in range(1, 40):
    b += a_mi[i]*a_mi[80 - i]
print(ans - b)
