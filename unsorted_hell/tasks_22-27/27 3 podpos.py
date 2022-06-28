f = open("27A (46).txt")
n = int(f.readline())
k = [0]*11

c = 0
k5 = 0
for i in range(n):
    x = int(f.readline())

    if x%5 == 0: k5 += 1
    if k5%11 == 0: c += 1
    c += k[ k5%11 ]

    k[ k5%11 ] += 1
    
print(c)
