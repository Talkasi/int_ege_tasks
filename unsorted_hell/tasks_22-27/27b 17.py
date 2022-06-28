f = open("27A (21).txt")
n = int(f.readline())
m = [[] for i in range(10)]

for i in range(n):
    x = int(f.readline())
    m[int(str(x)[0])] += [x]
mi = 182195673426573620
for i in range(1, 10):
    mi = min(mi, len(m[i]))
print(mi)
