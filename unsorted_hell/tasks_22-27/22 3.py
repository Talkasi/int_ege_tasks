
for s in range(1, 100000000000000):
    i = s
    P = 23
    Q = 7
    K1 = 0
    K2 = 0
    while s != 1350:
        s = s + P
        K1 = K1 + 1
        if s > 1350: break
    if s == 1350:
        while s != Q + K1:
            if s < Q + K1:
                break
            s = s - Q
            K2 = K2 + 1
        if s ==  Q + K1:
            K1 += s
            K2 += s
            if K1 == 19 and K2 == 204:
                print(i)
                break
