f = open("27-A (6).txt")
n, k = map(int, f.readline().split())
a = [int(x) for x in f]
stat = [[]*100 for x in range(100)]

for i in range(n):
    for j in range(1, int(a[i] ** 0.5) + 1):
        if a[i] % j == 0:
            stat[j].append(a[i])
            stat[a[i]//j].append(a[i])
print(stat)
