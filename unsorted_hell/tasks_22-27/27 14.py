f = open("27A (40).txt")
n = int(f.readline())
c = 0
ost = [110**1000]*144
mi = 10**1000
for i in range(n):
    x = int(f.readline())
    osty = x%144
    if osty != 0 and x > ost[144 - x%144]: mi = min(mi, x+ost[144 - x%144])
    elif osty == 0 and x > ost[x%144]: mi = min(mi, x+ost[x%144])
    ost[x%144] = min(x, ost[x%144]) 
print(mi)
    
