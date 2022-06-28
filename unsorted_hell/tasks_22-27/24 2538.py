s = open('24-5.txt').readline().replace('()', 'F')
s = s.replace(')', ' ')
s = s.replace('(', ' ')
m = ''
for i in s.split():
    m = max(i, m, key = len)
print(m, len(m))
