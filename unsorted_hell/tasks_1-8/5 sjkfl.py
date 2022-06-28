mi = 10**30
for i in range(1, 10000):
    n = bin(i)[2:]
    if i%2 == 0: n = '10'+n+'10'
    else: n = '1' + n + '00'
    n = int(n, 2)
    if n > 100:
        mi = min(mi, n)
print(mi)
