for i in range(1, 1000):
    x = i
    k = x % 6
    a, b = 0, 0
    while x > 0:
        d = x % 6
        if d == k: a += 1
        b += d
        x //= 6
    if a == 2 and b == 15: print(i)
