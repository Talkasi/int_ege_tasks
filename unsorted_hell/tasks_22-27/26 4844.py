f = open("26-68.txt")
n, t = map(int, f.readline().split())
sr, c = 0, 0
virus = []
time = []
for i in range(n):
    u, ti = map(int, f.readline().split())
    sr += u
    c += 1
    virus += [u]
    time += [ti]
sr = sr/c
print(virus, time)
