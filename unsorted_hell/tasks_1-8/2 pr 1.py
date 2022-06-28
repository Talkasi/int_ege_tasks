k = 0, 1

for x in k:
    for y in k:
        for z in k:
            for w in k:
                if ((not(x <= w)) or (y == z) or y) == 0:
                    print(x, y, z, w)
