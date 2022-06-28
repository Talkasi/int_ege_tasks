for n in range(1, 10000):
    r = bin(n)[2:]
    if r.count('1') > r.count('0'):
        r += '0'
    else:
        r = '11' + r 
    if r.count('1') > r.count('0'):
        r += '0'
    else:
        r = '11' + r
    if int(r, 2) > 500:
        print(n)
        break
