print("x, y, z")
k = 0, 1
for x in k:
    for y in k:
        for z in k:
            if not ((z or y) <= (x == z)):
                print(x, y, z)
