f = open("27-97b.txt")
n, k = map(int, f.readline().split())
stat = [0] * k
s, c = 0, 0
for i in range(n):
    x = int(f.readline())
    s += x
    if s % k == 0: c += 1
    c += stat[ s % k ]

    stat[ s % k ] += 1
print(c)
