f = open("27A (8).txt")
n = int(f.readline())
a = [int(x) for x in f]
c = 0
for i in range(n):
    for j in range(i+1, n):
        if (a[i]+a[j])%80 == 0 and (a[i] > 50000 or a[j]>50000):
            c+=1
print(c)
