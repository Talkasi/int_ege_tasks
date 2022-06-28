for i in range(1, 10000):
    s = i
    n = 1
    while s < 185:
        s = s + 30
        n = n * 3
    if n == 729:
        print(i)
