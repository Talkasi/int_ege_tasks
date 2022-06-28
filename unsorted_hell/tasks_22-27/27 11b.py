f = open('27A (13).txt')
n = int(f.readline())
k = []
k31 = []
for i in range(n):
    x = int(f.readline())
    if x%31 == 0: k31 += [x]
    else: k += [x]
k.sort()
k31.sort()
print(k31[0]*k[0])
