m = 10**90
for i in range(1, 100000):
    n = bin(i)[2:]
    n = n + str(n.count("1")%2)
    n = n + str(n.count("1")%2)
    n = int(n, 2)
    if n > 396: m = min(n, m)
print(m)
print(8192 * (9+36)/1024)
