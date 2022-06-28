k = 0,1
for x in k:
    for y in k:
        for z in k:
            if not((x <= z) and not(x and y and z)):
                print(x, y, z)
