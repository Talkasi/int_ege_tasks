f = open("27a (43).txt")
n = int(f.readline())
a = [int(f.readline()) for i in range(n)]
mi = 10000000000000000000000000000000
for i in range(n):
    for j in range(i+5, n, 5):
        if (a[i] + a[j])%107 == 0:
            mi = min(mi, a[i] + a[j])
print(mi)

print(n)
