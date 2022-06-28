f = open("26 (19).txt")
n = int(f.readline())
a = sorted(int(x) for x in f)
print(len(a), max(a))
c = 0
m = max(a)
for i in range(len(a)):
    for j in range(i+1, len(a)):
        if (a[i] + a[j]) % 2 == 0:
            sr = (a[i] + a[j])//2
            if a[n//2 - 1] < sr < a[n//4 * 3]:
                c += 1
                m = min(sr, m)
print(c, m)
