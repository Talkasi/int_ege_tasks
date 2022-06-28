f = open("27B (24).txt")
n = int(f.readline())
c, c7 = 0, 0
for i in range(n):
    x = int(f.readline())

    if x%7==0: c += i
    if x%7!=0: c += c7

    if x%7 == 0: c7 += 1

print(c)
