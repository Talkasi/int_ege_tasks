f = open("24-1.txt")
s = f.readline().strip()
for i in set(s):
    if i not in '1234567890':
        s = s.replace(i, ' ')
s = s.split()
print(min(int(x) for x in s if int(x)%2!=0))
