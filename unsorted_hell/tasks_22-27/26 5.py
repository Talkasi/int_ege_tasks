f = open("26 (20).txt")
n = int(f.readline())
c, m = 0, 0
a = sorted(int(x) for x in f)
b = set(a)
print(n)
ans = []
for i in range(n):
    for j in range(i+1, n):
        if a[i]%2 != a[j]%2:
            s = a[i] + a[j]
            if s in b:
                ans.append(s)

print(len(ans), max(ans))
