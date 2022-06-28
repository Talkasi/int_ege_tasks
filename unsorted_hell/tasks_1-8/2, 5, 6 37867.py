k = 0, 1
for x in k:
    for y in k:
        for z in k:
            for w in k:
                if ((x or y) and (y != z) and (not(w))):
                    print(x, y, z, w)

for i in range(501, 100000):
    n = bin(i)[2:]
    n = n[::-1]
    n = int(n, 2)
    if n == 15:
        print(i)
        break

s = 0
n = 0
while s < 111:
    s = s + 8
    n = n + 2
print(n)
