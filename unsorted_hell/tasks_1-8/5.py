m = 0
for i in range(1, 10000):
    n = bin(i)[2:]
    if i % 2 == 0: n = '1' + n + '00'
    else: n  = '10' + n + '1'
    n = int(n, 2)
    if n < 1000:
        m = max(m, i)
        print(i)
print(m)
