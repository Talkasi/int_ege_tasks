f = open("27A (15).txt")
n = int(f.readline())
a = [int(x) for x in f]
m = 0
for i in range(n):
    for j in range(i+1, n):
        if (a[i]+a[j]) % 2==0 and (a[i]%23==0 or a[j]%23==0):
            m = max(m, a[i]+a[j])
print(m)
