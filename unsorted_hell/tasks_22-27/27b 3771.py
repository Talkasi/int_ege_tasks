f = open('27-52b.txt')
n = int(f.readline())
k0 = []
k1 = []
k2 = []
for i in range(n):
    x = int(f.readline())
    if x%3 == 0: k0 += [x]
    if x%3 == 1: k1 += [x]
    if x%3 == 2: k2 += [x]
k0.sort()
k1.sort()
k2.sort()
print(max(k0[-1]+k0[-2]+k0[-3], \
          k1[-1]+k2[-1]+k0[-1], \
          k1[-1]+k1[-2]+k1[-3], \
          k2[-1]+k2[-2]+k2[-3]))
    
