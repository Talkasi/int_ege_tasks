for i in range(100_0000, 1, -1):
    x = i
    l = 0
    m = 1
    while x > 0:
        l += 1
        m = m * (x % 8)
        x = x//8
    if l == 3 and m == 120:
        print(i)
        break
