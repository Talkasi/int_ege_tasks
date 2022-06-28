for i in range(401, 500):
    s = i*'5'
    while '5555' in s:
        s = s.replace('5555', '8', 1)
        s = s.replace('88', '5', 1)
    print(s, i)
