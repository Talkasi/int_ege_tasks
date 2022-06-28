f = open("27A (59).txt")
n, k = map(int, f.readline().split())
a = [int(x) for x in f]
print(len(a))
'''
n, k = 6, 30
a = [8, 20, 5, 13, 7, 19]'''
mk = -10**29
for i in range(n):
    s = 0
    c = 0
    for j in range(i, n):
        s += a[j]
        c += 1
        if s < k:
            mk = max(mk, c)
print(mk)
