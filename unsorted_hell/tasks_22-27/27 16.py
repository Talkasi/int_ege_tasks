f = open('27A (29).txt')
n = int(f.readline())
m = [0]*100
ma = 0

for i in range(n):
    x = int(f.readline())

    if x%100 <= 12:
        if x < m[12 - x%100]:
            ma = max(ma, x + m[12 - x%100])
    else:
        if x < m[112 - x%100]:
            ma = max(ma, x + m[112 - x%100])

    m[x%100] = max(x, m[x%100])

print(ma)
