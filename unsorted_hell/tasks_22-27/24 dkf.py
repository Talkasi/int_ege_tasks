s = open("24-3 (1).txt").readline()
#s = '9dfglgDJFD97654090909'
a = s[0]
m = ''
for i in range(len(s) - 1):
    if s[i] > s[i+1]:
        a += s[i+1]
    else:
        m = max(m, a, key = len)
        a = s[i + 1]
m = max(m, a, key = len)
print(m, len(m))
