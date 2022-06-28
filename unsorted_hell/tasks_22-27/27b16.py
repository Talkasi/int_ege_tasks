f = open("27A (20).txt")
n = int(f.readline())
su = [[] for i in range(9*5 + 1)]
for i in range(n):
    x = int(f.readline())
    su[sum(int(i) for i in str(x))] += [x]
m = 0
for i in range(46):
    m = max(m, len(su[i]))
print(m)
