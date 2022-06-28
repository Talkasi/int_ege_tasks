for a in range(1, 1000):
    if all( (5*x - 6*y < a) or (x - y > 30) for x in range(10000) for y in range(10000)):
        print(a)
