for x in '0123456789':
    for y in '0123456789':
        s = '1' + x + '34567' + y +'9'
        s = int(s)
        if s % 17 == 0:
            print(s, s//17)
