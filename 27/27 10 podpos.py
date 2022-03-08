f = open("27A (51).txt")
n = int(f.readline())
q = []
k7 = 0
s = 0
for i in range(6):
    x = int(f.readline())
    s += x
    if x > 0 and x % 7 == 0: k7 += 1
    q.append( [s, k7] )

statsum = [10**20] * 7
ms = -10**20
for i in range(n - 6):
    x = int(f.readline())
    s += x

    if x > 0 and x % 7 == 0: k7 += 1
    #Special case
    if k7 % 7 == 0: ms = max(s, ms)
    ms = max(ms, s - statsum[ k7 % 7 ])

    #Stat
    sumq0, k7q0 = q[0]
    statsum[ k7q0 % 7 ] = min(sumq0, statsum[ k7q0 % 7 ])

    q.pop(0)
    q.append( [s, k7] )
print(ms)
