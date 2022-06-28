c = 0
for b in range(1, 100_001):
    x = 1019
    y = b
    st = 0
    while x != y:
        if x < 1019: break
        if y < 1019:
            st = 1
            break
        if x > y:
            x -= y
        else:
            y -= x
    if st == 0 and x == 1019:
        print(1019, b)
        c += 1
print(c)
