for a in range(1, 1000):
    if all(((2*y + 3*x != 135) or (y > a) or (x > a)) for x in range(1, 700) for y in range(1, 700)):
        print(a)
