f = open("27A (25).txt")
n = int(f.readline())
k5, k13, k65, c = 0, 0, 0, 0
for i in range(n):
    x = int(f.readline())

    if x%65 == 0: c += i
    elif x%13 == 0: c += k5
    elif x%5 == 0: c += k13
    else: c += k65

    if x%5 == 0: k5 += 1
    if x%13 == 0: k13 += 1
    if x%65 == 0: k65 += 1
print(c)
