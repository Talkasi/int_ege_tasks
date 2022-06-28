s = open("24-1 (1).txt").readline().strip()
c = s[0]
m, mi = '', 1
for i in range(len(s) - 1):
    if s[i] < s[i+1]:
        c += s[i+1]
    else:
        if len(m) < len(c):
            m = c
            mx = mi
        mi = i + 1 + 1
        c = s[i+1]
m = max(c, m, key = len)
print(len(m), m, mx, s[49233:49240])
