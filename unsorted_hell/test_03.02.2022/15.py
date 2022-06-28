for a in range(1, 100000):
    if all( (x&30 != 4) or ((x&35 == 1) <= (x&a == 0)) for x in range(1, 1000000)):
        print(a)
