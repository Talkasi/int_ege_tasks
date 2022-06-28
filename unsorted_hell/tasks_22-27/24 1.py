s = open('24 (12).txt').readline()
c = ''
m = '9'*len(s)
for i in range(len(s)):
    if s[i]!='A':
        c += s[i]
    else:
        if c!='': m = min(m, c, key = len)
        c = ''
print(m, len(m))
