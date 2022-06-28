m = 0
for s in open('24-171.txt'):
    s = s.strip()
    s = s.replace('XYZ', '%')
    for i in set(s):
        if i != '%':
            s = s.replace(i, ' ')
    for i in s.split(' '):
        m = max(len(i), m)
print(m * 3)
