for x in range(1, 1000):
    s = x
    n = 1
    while s <= 70:
        s = s + 9
        n = n * 7
    if n == 343: print(x)
