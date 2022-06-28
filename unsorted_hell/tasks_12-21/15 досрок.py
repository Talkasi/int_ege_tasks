for a in range(1, 100):
    if all(((x%2 == 0) <= (x%5!=0)) or (x + a >= 80) for x in range(1, 1000)):
        print(a)
