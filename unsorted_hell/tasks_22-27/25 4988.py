for i in range(500, 1000000000):
    if 169*i > 10**9: break
    s = str(169*i)
    if len(s) > 6 and s[0:3] == '123' and s[-4:-1] == '567':
        print(169*i, i)
