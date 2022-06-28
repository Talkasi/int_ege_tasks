k = 0, 1
for x in k:
    for y in k:
        for z in k:
            for w in k:
                if (w <= y) and ((x <= z)==(y<=x)):
                    print(x, y, z, w)
