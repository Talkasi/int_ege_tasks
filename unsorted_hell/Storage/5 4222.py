m = 0
for n in range(1, 10000):
    r = hex(n//2)[2:]
    if n%4 != 0:
        r = 'F' + r + 'A0'
    else:
        r = '15' + r + 'C'
    if int(r, 16) < 65536:
        m = max(m, n)
print(m)
