f = open("27A (35).txt")
n = int(f.readline())
ma230 = []
ma231 = []
man230 = 0
man231 = 0

for i in range(n):
    x = int(f.readline())
    if x%23 == 0 and x%2 == 0: ma230.append(x)
    if x%23 == 0 and x%2 != 0: ma231.append(x)
    if x%23 != 0 and x%2 == 0: man230 = max(man230, x)
    if x%23 != 0 and x%2 != 0: man231 = max(man231, x)
ma230.sort()
ma231.sort()
print(max(ma230[-1]+ma230[-2], \
          ma230[-1]+man230, \
          ma231[-1]+ma231[-2], \
          ma231[-1]+man231))
