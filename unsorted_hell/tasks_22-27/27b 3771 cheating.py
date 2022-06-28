f = open('27-52b.txt')
n = int(f.readline())

a = [int(x) for x in f]
a.sort()
a = a[-300:]
m = 0
n = 300
for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            if (a[i]+a[j]+a[k]) %3 ==0:
                m = max(m, a[i]+a[j]+a[k])
print(m)
