for i in range(1, 10000000000):
    x = i
    a = 0
    b = 1
    while x > 0:
        a = a + 1
        b = b * (x % 10)
        x = x // 10
    if a == 2 and b == 72:
        print(i)
