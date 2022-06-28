f = open("27B (38).txt")
n = int(f.readline())
q = [int(f.readline()) for i in range(5)]
c = 0
kost = [0]*10
print(kost[1] + 1)
for i in range(n - 5):
    x = int(f.readline())
    ost = x%10
    if ost == 1: c += kost[3]
    if ost == 3: c += kost[1]
    if ost == 7: c += kost[9]
    if ost == 9: c += kost[7]

    
    kost[q[0]%10] += 1
    q.pop(0)
    q.append(x)
print(c)
    
