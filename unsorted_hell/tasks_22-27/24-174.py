m = ''
c = 0
for s in open('24-174.txt'):
    s = s.strip()
    if s.count('R') < 30:
        for i in set(s):
            n = s.replace(i, ' ').split()
            if s[0] != i:
                n[0] = ''
            if s[-1] != i:
                n[-1] = ''
            for j in n:
                if len(j) > 0:
                    m = max(m, i + j + i, key = len)
                    c += 1
print(len(m) - 1, c)
