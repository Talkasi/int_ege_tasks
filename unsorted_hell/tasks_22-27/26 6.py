f = open("26 (21).txt")
n = int(f.readline())
a = sorted(int(x) for x in f)

c = len(set(a))

c1, m = 1, 0
for i in range(len(a) - 1):
    if a[i] == a[i+1]:
        c1 += 1
    else:
        m = max(m, c1)
        c1 = 1
print(c, m)
