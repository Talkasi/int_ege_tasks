for i in range(1,10000):
    for j in range(1, 10000):
        x = i
        y = j
        a = 0
        b = 0
        while x > 0 or y > 0:
            if x > 0:
                a = a + 1
            if y > 0:
                b = b + 1
            if a > 6 or b > 7: break
            x = x // 2
            y = y // 10
        if a == 6 and b == 7:
            print(i*j)
