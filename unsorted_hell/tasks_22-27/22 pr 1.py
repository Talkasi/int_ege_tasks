for i in range(1, 1000000):
    x = i
    q, p, k1, k2 = 8, 10, 0, 0
    while x <= 100:
        k1 += 1
        x += p
    while x >= q:
        k2 += 1
        x = x - q

    l = x + k1
    m = x + k2
    if l == 12 and m == 19: print("ans", i)
