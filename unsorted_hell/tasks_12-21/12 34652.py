
for i in range(91, 153):
    s = '1'*i
    while '111' in s:
        s = s.replace('111', '2', 1)
        s = s.replace('2222', '333', 1)
        s = s.replace('33', '1', 1)
    #print(s, i, s.count('1'))

s = (12 ** 34) + 7 * (12 ** 26) - 3 * (12 ** 16) + 2 * (12 ** 5) + 552
d = set()
while s > 0:
    d.add(s % 12)
    s = s//12
print(len(d), d)
