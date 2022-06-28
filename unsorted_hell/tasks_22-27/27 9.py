f = open("27A (36).txt")
n = int(f.readline())
q = [int(f.readline()) for i in range(8)]
print(q)
c, k, k23 = 0, 0, 0
for i in range(n - 8):
    x = int(f.readline())
    if x%23 == 0: c += k
    else: c += k23

    if q[0]%23 == 0: k23 += 1
    k += 1
    q.pop(0)
    q.append(x)
print(c)
    
