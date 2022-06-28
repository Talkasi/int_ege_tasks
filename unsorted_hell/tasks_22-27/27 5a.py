f = open("27A (4).txt")
n = int(f.readline())
a = [int(x) for x in f]
c = 0
for i in range(n):
    for j in range(i+1, n):
        for m in range(j+1, n):
            if a[i]%19==0 and a[j]%19==0 and a[m]%19 == 0:
                c+=1
print(c)
