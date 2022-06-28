for a in range(1, 100):
    if all((2*y + x < a) or (x > 10) or (y > 25) for x in range(1, 1000) for y in range(1, 1000)):
        print(a)
