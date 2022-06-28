f = open("27A (37).txt")
n = int(f.readline())
q = [int(f.readline()) for i in range(4)]
print(q)
c = 0
kn, k13ch = 0, 0
kch, k13nch = 0, 0
for i in range(n - 4):
    x = int(f.readline())
    if x%13 == 0 and x%2 == 0: c += kn
    if x%13 == 0 and x%2 != 0: c += kch
    if x%13 != 0 and x%2 == 0: c += k13nch
    if x%13 != 0 and x%2 != 0: c += k13ch

    if q[0]%2 == 0: kch += 1
    else: kn += 1
    if q[0]%26 == 0: k13ch += 1
    elif q[0]%13 == 0: k13nch += 1

    q.pop(0)
    q.append(x)
print(c)
    
