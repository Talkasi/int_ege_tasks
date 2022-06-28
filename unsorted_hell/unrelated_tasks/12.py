for i in range(301, 10000):
    s = '5' * i
    while '55555' in s:
        s = s.replace('55555', '88', 1)
        s = s.replace('888', '55', 1)
    
    if s.count('5') == 6:
        print(s.count('5'), i)
        break
