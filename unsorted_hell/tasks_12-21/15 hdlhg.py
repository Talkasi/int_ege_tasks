for a in range(100000, 1, -1):
    if all((x < a and y < a and x*y > 1200) == 0 for x in range(1, 2000) for y in range(1, 2000)):
        print(a)
