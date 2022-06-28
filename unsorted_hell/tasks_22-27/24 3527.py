s = open('24-153.txt').readline().strip()
print(set(s))
for i in set(s):
    if i != 'D':
        s = s.replace(i, ' ')
print(s[:100])
s = s.split()
print(s[:100])
print(min(s), len(min(s)))
