f = open('24-171.txt')
m = 0
for s in f:
    c = s.replace('XYZ', '*')
    for i in set(c):
        if i != '*': c = c.replace(i, ' ')
    c = c.split()

    len1 = len(max(c)) * 3
    if ('XYZ' * (len1 // 3) + 'X') in s: len1 = len1 + 1


    c = s.replace('ZXY', '*')
    for i in set(c):
        if i != '*': c = c.replace(i, ' ')
    c = c.split()

    if ('ZXY' * (len(max(c)) // 3) + 'Z') in s: len3 = len(max(c)) * 3 + 1
    if ('ZXY' * (len(max(c)) // 3) + 'ZX') in s: len3  = len(max(c)) * 3 + 2

    m = max(m, len1, len3)

print(m)
