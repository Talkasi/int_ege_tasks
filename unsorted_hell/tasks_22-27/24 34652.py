s = open("24-157 (2).txt").readline().strip()
c, m = s[0], ''
for i in range(len(s) - 1):
    if (s[i]+s[i+1]) != 'PR' and (s[i]+s[i+1]) != 'RP':
        c += s[i + 1]
    else:
        m = max(m, c, key = len)
        c = s[i+1]
m = max(m, c, key = len)
print(len(m))

s = 9**7 + 3 ** 21 - 8
c = 0
while s >0:
    c+= s % 3
    s = s//3
print(c)
