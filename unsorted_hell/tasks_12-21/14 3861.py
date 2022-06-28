v = 27 ** 7 - 3**11 +36
for x in range(1, 1000000):
    s = v - x
    c = 0
    while s>0:
        c += s%3
        s = s//3
    if c == 22:
        print(x)
        break
