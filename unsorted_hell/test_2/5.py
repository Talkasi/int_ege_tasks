c = 0
for n in range(2, 10000):
    r = bin(n)[2:]
    r += r[-2]
    r += r[1]
    r = int(r, 2)
    if 150 <= r <= 250:
        print(r)
        c += 1
print()
print(c)
