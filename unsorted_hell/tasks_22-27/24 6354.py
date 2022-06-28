s = open("24-2.txt").readline()
print(s[44700], s[44700:44708])
c, n, m = s[0], 1, ''
for i in range(len(s) - 1):
    if s[i] > s[i+1]:
        c += s[i+1]
    else:
        if len(c) > len(m):
            m = c
            mn = n
        n = i + 2
        c = s[i + 1]
print(mn, m)

for i in range(1, 257):
    n = bin(i - 1)[2:]
    while len(n) < 8:
        n = '0' + n
    n = n.replace('0', '=')
    n = n.replace('1', '0')
    n = n.replace('=', '1')
    n = int(n, 2)
    if n == 143:
        print(i)

for i in range(1, 10000000):
    s = i
    n = 50
    while s > 0:
        s = s//2
        n = n - 3
    if n == 23:
        print(i)
        break
