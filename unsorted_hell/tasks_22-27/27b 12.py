f = open("27B (15).txt")
k23_0 = []
k23_1 = []
k_0 = []
k_1 = []
n = int(f.readline())
for i in range(n):
    x = int(f.readline())
    if x%46 == 0: k23_0 += [x]
    elif x%23 == 0: k23_1 +=[x]
    elif x%2 == 0: k_0 += [x]
    else: k_1 += [x]
k_0.sort()
k_1.sort()
k23_1.sort()
k23_0.sort()
print(max(k_0[-1]+k23_0[-1], k_1[-1]+k23_1[-1],k23_1[-1]+k23_1[-2], k23_0[-1]+k23_0[-2]))
