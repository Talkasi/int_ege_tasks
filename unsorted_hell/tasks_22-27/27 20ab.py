f = open('27B (18).txt')
n = int(f.readline())
k1 = k2 = k3 = 0
for i in range(n):
    x, y = map(int, f.readline().split())
    if y == 0 and x != 0: k1 += 1
    elif y != 0 and x == 0: k2 += 1
    else: k3 += 1

print(k1*k2*k3)
