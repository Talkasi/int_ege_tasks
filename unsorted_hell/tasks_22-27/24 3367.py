s = open('24-3.txt').readline()

c = s[0]
m = ''
for i in range(len(s) - 1):
    if s[i] < s[i+1]:
        c += s[i+1]
    else:
        m = max(m, c, key = len)
        c = s[i]
print(m, len(m))
