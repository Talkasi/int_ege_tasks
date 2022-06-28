s = open("24-j2.txt").readline()
m = ''
for a in 'FAIL':
    c = s
    for x in 'FAIL':
        if x != a:
            c = c.replace(x, ' ')
    c = c.split()
    m = max(c, m, key = len)
print(m)
