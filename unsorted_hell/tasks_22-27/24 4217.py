s = open('24-157.txt').readline()
c, m = s[0], ''

for i in range(len(s) - 1):
    if s[i]+s[i+1] != 'QW':
        c += s[i+1]
    else:
        m = max(c, m, key = len)
        c = s[i]
print(m, len(m))
