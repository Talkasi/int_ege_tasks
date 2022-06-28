f = open("26 (22).txt")
n = int(f.readline())
r = [0] * 2_000_000
for s in f:
    a, b = map(int, s.split())
    for i in range(a-1, b - 1):
        r[i] = 1
m = 0
for i in range(len(r) - 1):
    if r[i] == 0 and 1 == r[i+1]:
        m += 1
print(m, r.count(1))

