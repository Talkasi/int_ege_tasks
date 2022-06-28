f = open("27A (59).txt")
n, k = map(int, f.readline().split())
s, c, ml = 0, 0, 0
q = []
'''n, k = 6, 30
a = [8, 20, 5, 13, 7, 19]'''
for i in range(n):
    x = int(f.readline())
    s += x
    c += 1

    if s <= k: ml = max(ml, c)
    else:
        if len(q) != 0:
            if s - q[0] > k: q.pop(0)
            while s - q[0] > k:
                q.pop(0)
    ml = max(ml, len(q))

    q.append(s)
print(ml)
