f = open('27A (33).txt')
n = int(f.readline())
# sum%23 == 0 and pr%6 == 0 and r >= 7
# 0 - %6; 1 - %2; 2 - %3, 3 - all
a = [[100**100]*23 for i in range(4)]
mi = 100**100
q = [int(f.readline()) for i in range(6)]
for i in range(n - 6):
    x = int(f.readline())
    ost = (23 - x%23) if x%23 != 0 else 0
    if x%6 == 0:
        mi = min(a[3][ost]+x, mi)
    elif x%3 == 0:
        mi = min(a[1][ost]+x, mi)
    elif x%2 == 0:
        mi = min(a[2][ost]+x, mi)
    else:
        mi = min(a[0][ost]+x, mi)

    if q[0]%6 == 0: a[0][q[0]%23] = min(a[0][q[0]%23], q[0])
    if q[0]%2 == 0: a[1][q[0]%23] = min(a[1][q[0]%23], q[0])
    if q[0]%3 == 0: a[2][q[0]%23] = min(a[2][q[0]%23], q[0])
    a[3][q[0]%23] = min(a[3][q[0]%23], x)

    q.append(x)
    q.pop(0)
print(mi)
