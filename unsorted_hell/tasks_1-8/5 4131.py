for i in range(2, 100):
    n = bin(i)[3:]
    n = n.replace('1', '-')
    n = n.replace('0', '1')
    n = n.replace('-', '0')
    n = '1' + n
    if (i+int(n, 2)) > 99 and i%2!=0:
        print(i)
