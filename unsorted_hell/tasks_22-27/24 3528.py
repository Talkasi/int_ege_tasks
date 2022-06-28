s = open('24-153.txt').readline()
s = s.replace('D', ' ')
m = s
for i in s.split():
    m = min(m, i, key = len)
print(m, 2 + len(m))
