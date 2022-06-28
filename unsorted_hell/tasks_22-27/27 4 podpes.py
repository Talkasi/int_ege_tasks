f = open("27_A.txt")
n = int(f.readline())
k = [100**1000]*3
k5 = 0
s = 0
sm = 0
for i in range(n):
    x = int(f.readline())
    s += x
    if x%5 == 0: k5 += 1
    if k5%3 == 0: sm = max(sm, s)
    sm = max(sm, s - k[ k5%3 ])

    k[ k5%3 ] = min(k[k5%3], s)
print(sm)
