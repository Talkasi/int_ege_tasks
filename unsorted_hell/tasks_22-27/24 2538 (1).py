s = open('24-5.txt').readline()
c = 0
m = 0
i = 0
while i < len(s):
    if s[i:i+2]=='()':
        c += 1
        i += 2
    else:
        m = max(c, m)
        c = 0
        i += 1
print(m)
