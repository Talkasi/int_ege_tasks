for i in range(1, 1000):
    a = i
    r = 9
    l = 0
    while a >= r:
        l = l + 1
        a = a - r
    m = a
    if m < l:
        m = l
        l = a
    if l == 2 and m == 8:
        print(i)
        
