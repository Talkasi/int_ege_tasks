k = 0, 1
for x in k:
    for y in k:
        for z in k:
            if ((y <= z) and not(z and x)):
                print(x, y, z)
