f = open("27B (1).txt")
n = int(f.readline())

c7 = c = 0
for i in range(n):
    x = int(f.readline())
    if x%7 == 0: c7 += 1
    else: c += 1
print(c7*(c7 - 1)//2 + c*c7)
