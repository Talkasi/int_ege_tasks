f = open("27B (40).txt")
n = int(f.readline())
q = []
c = 0
print(q, len(q))
for i in range(n):
    x = int(f.readline())
    for j in range(len(q)):
        if (q[j]+x)%8 != 0:
            c += 1
    q.append(x)
    if len(q) > 7: q.pop(0)
print(c)
    
