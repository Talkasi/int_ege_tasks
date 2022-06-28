s = open("24-2 (2).txt").readline()
c, n, m = s[0], 1, ''
for i in range(len(s) - 1):
    if s[i] < s[i+1]:
        c += s[i+1]
    else:
        m = max(m, c, key = len)
        c = s[i + 1]
m = max(m, c, key = len)
print(m, len(m))

c = 1
for n in range(3532000, 3532161):
    if all(n%x != 0 for x in range(2, int(n**0.5) + 1)):
        print(c, n)
        c+=1
