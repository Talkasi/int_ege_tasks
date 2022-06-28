s = open('24-181.txt').readline()
s = s.split('.')
m = ''

for i in range(len(s) - 1):
    m = max(m, s[i] + '.' + s[i+1], key = len)

print(m, len(m))
