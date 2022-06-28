for i in range(10000, 0, -1):
    s = i
    n = 12
    while s > 0:
        s = s - 10
        n = n + 7
    if n == 61:
        print(i)
