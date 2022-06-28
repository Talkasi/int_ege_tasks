k = 0,1
for x in k:
    for y in k:
        for z in k:
            for w in k:
                if ((not(x <= y)) or ((not(w)) <= (not(z))) or w) == 0:
                    print(x, y, z, w)
