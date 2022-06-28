f = open("27A (45).txt")
n = int(f.readline())
m = [0]*666
s = 0
c = 0
for i in range(n):
    x = int(f.readline())
    s += x
    if s%666 == 0: c += 1
    #ost = 666 - s%666 if s%666!= 0 else 0
    
    c += m[ s%666 ]
    m[s%666] += 1
print(c, n)
