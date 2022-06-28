f = open("27A (22).txt")
n = int(f.readline())
m = [[] for i in range(10)]

for i in range(n):
    x = int(f.readline())
    for i in str(x):
        m[int(i)] += [90]
mi = 215374214008412
for i in range(10):
    mi = min(mi, len(m[i]))
print(mi)
