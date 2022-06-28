f = open("27A (58).txt")
n = int(f.readline())
k, k5 = 0, 0
stat = [0] * 11

for i in range(n):
    x = int(f.readline())
    if x % 5 == 0: k5 += 1
    if k5 != 0 and k5 % 11 == 0: k += 1
    k += stat[ k5 % 11 ]

    stat[k5 % 11] += 1
print(k)
