for x in '0123456789':
    for y in '0123456789':
        i = '12345'+x+'7'+y+'8'
        i = int(i)
        if i%23 == 0:
            print(i, i//23)
