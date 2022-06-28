f = open('27-52a.txt')
n = int(f.readline())
a = [int(x) for x in f]
m = 0
for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            if (a[i]+a[j]+a[k]) %3 ==0:
                m = max(m, a[i]+a[j]+a[k])

print(m)
