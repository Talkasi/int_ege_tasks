f = open("27A (3).txt")
n = int(f.readline())
c5_0 = c_0 = c_1 = c5_1 = 0
for i in range(n):
    x = int(f.readline())
    if x%5 == 0 and x%2 == 0: c5_0 += 1
    if x%5 == 0 and x%2 != 0: c5_1 += 1
    if x%5 != 0 and x%2 == 0: c_0 += 1
    if x%5 != 0 and x%2 != 0: c_1 += 1
print(c5_0*c5_1 + c5_0*c_1 + c5_1*c_0)
