for x in range(1, 100000):
    z = x
    a, b = 0, 0
    while x > 0:
        a += 1
        if x % 2 == 0:
            b += x % 10
        x = x//10
    if a == 3 and b == 18:
        print(z)
