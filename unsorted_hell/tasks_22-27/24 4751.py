s = open('24-181.txt').readline().replace('.', ' ').split()
for i in range(len(s)):
    if 'Y' in s[i]:
        s[i] = ''
        
c = ''
m = ''
n = 0
for i in range(len(s)):
    if s[i]!='' and c.count('.')<= 5:
        c += s[i] + '.'
    else:
        if c != '':
            m = max(m, c[:-1], key = len)
        n = 0
        c = ''
print(m, len(m), len(s))
        
