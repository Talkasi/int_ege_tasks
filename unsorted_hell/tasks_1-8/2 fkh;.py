k = 0, 1

for x in k:
    for y in k:
        for z in k:
            for w in k:
                if ((not(w)) and ((y or z) <= (y and (not(x))))):
                    print(x, y, z, w)
