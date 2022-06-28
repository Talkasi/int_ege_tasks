m = ''
c = 0
for s in open('24-174.txt'):
    if s.count('R') < 30:
        for i in set(s):
            n = s.replace(i, i + ' ' + i).split()
            for j in n:
                if len(j) > 2 and j[0] == j[-1]:
                    m = max(m, j, key = len)
                    c += 1
print(len(m) - 1, c)
