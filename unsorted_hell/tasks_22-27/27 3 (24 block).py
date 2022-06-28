f = open("27B (26).txt")
n = int(f.readline())
c, k0, k1, k5_1, k5_0 = 0, 0, 0, 0, 0
for i in range(n):
    x = int(f.readline())

    if x%5 == 0 and x%2 == 0: c += k1
    if x%5 == 0 and x%2 != 0: c += k0
    if x%5 != 0 and x%2 != 0: c += k5_0
    if x%5 != 0 and x%2 == 0: c += k5_1

    if x%2 == 0: k0 += 1
    if x%2 != 0: k1 += 1
    if x%5 == 0 and x%2 == 0: k5_0 += 1
    if x%5 == 0 and x%2 != 0: k5_1 += 1
print(c)
