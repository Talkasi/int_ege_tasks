for i in range(1, 100000):
    x = i
    a, b = 0, 0
    while x > 0:
        if x % 2 == 0:
            a += 1
        else:
            b += x % 6
        x = x//6
    if a == 1 and b == 4:
        print(i)
        break
