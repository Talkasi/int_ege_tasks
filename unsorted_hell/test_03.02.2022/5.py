for n in range(1, 100):
    x = bin(n)[2:]
    if x.count('1') > x.count('0'):
        x = x + '0'
    else:
        x = '11' + x

    if x.count('1') > x.count('0'):
        x = x + '0'
    else:
        x = '11' + x

    x = int(x, 2)
    if x > 500:
        print(n)
