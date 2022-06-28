f = open("26 test.txt")
n = int(f.readline())
a = sorted(int(x) for x in f)
w = [0]*(sum(a)+1)

for i in range(n):
    w1 = w.copy()
    for j in range(len(w)):
        if w[j] > 0:
            w[a[i] + j] += w[j]
    w1[ a[i] ] += 1
    w = w1
c = 0
k = 0

for i in range(n):
    if w[i] == 0:
        c += a[i]
        k += 1
print(m, w[m])
