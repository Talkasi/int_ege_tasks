k = 0, 1
for x in k:
    for y in k:
        for z in k:
            for w in k:
                if ((x or y) and y != z and not (w)):
                    print(x, y, z, w)
