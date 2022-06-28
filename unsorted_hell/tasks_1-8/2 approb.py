print("x y z w")
k = 0, 1
for x in k:
    for y in k:
        for z in k:
            for w in k:
                if not( (w == z) or (x and not(y)) or w):
                    print(x, y, z, w)
