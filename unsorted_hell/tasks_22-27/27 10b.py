f = open('27B (12).txt')
n = int(f.readline())
ma_0 = []
ma_1 = []

for i in range(n):
    x = int(f.readline())
    if x%2 != 0: ma_1 += [x]
    if x%2 == 0: ma_0 += [x]

ma_0.sort()
ma_1.sort()

print(ma_0[-1] + ma_1[-1])
