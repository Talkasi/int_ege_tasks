f=open('27A (30).txt')
n=int(f.readline())
m=[[10**20]*1071 for i in range(2)]
ms=10**20

for i in range(n):
    x=int(f.readline())
    for j in range(i+1,i+12):
        ost=1071-x%1071 if x%1071!=0 else 0
        if x%2==0:
            ms=min(ms,x + m[0][ost])
        if x%2!=0:
            ms=min(ms,x+m[1][ost])

    if x%2==0:
        m[0][x%1071]=min(m[0][x%1071],x)
    if x%2!=0:
        m[1][x%1071]=min(m[1][x%1071],x)
print(ms)
