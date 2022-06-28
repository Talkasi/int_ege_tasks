for i in range(1, 100000):
    n = 34
    s = i
    while n <= 170:
        s = s+120
        n = n+23
    if 1000 <= s <= 9999:
        print(i)
        break
