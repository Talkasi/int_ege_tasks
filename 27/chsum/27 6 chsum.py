#number of groups%10==5.
f = open("27A (57).txt")
n = int(f.readline())
k = [0]*10
for i in range(n):
    x = int(f.readline())
    k1 = k.copy()
    for j in range(10):
        k1[(x+j)%10] += k[j]
    k1[x%10] += 1
    k = k1
print(k[5])
