f = open("27A (2).txt")
n = int(f.readline())
c = c5 = c13 = c65 = 0
#5 13
for i in range(n):
    x = int(f.readline())
    if x%5 == 0 and x%13 == 0: c65 += 1
    if x%5 == 0 and x%13 != 0: c5 += 1
    if x%5 != 0 and x%13 == 0: c13 += 1
    if x%5 != 0 and x%13 != 0: c += 1

print((n-c65)*c65 + c65*(c65-1)//2 +c5*c13)
    
