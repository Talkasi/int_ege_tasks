f = open('27A (23).txt')
n = int(f.readline())
c = 0
a = [[0]*80 for i in range(2)]
for i in range(n):
    x = int(f.readline())
    ost = 80 - x%80 if x%80 != 0 else 0
    if x>50_000:
        c += a[0][ost] + a[1][ost]
    if x<=50_000:
        c += a[1][ost]

    if x>50_000:
        a[0][x%80] += 1
    else:
        a[1][x%80] += 1
print(c)
        
