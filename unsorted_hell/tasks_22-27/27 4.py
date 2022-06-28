f = open("27A (27).txt")
n = int(f.readline())
c = 0
k = [0]*131
for i in range(n):
    x = int(f.readline())
    ost = 131 - x%131 if x%131 != 0 else 0
    c += k[ost]

    k[x%131] += 1
print(c)
