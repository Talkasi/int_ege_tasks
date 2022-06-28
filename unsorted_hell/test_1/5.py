for i in range(1, 100):
    n = bin(i)[2:]
    r = n + n[-1]
    if n.count('1')%2==0: r+='0'
    else: r+= '1'
    
    if r.count('1')%2==0: r += '0'
    else: r += '1'
    r = int(r, 2)
    if r > 105:
        print(r)
