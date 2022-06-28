m = 0
for n in range(1, 1000):
    r = bin(n)[2:]
    if n%2 == 1:
        r += '0'
    else:
        r = '11' + r + '11'
    if int(r, 2) < 126:
        m = max(m, int(r, 2))
print(m)
