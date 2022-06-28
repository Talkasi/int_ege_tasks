for a in range(1, 10000000):
    if all(((x%3 == 0) <=(not(x%5 == 0))) or (x + a >= 90) for x in range(1, 1000)):
        print(a)
        break
