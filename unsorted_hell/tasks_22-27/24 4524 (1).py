s = open('24-181.txt').readline().split('.')
m = 0
for i in range(len(s) - 1):
    m = max(len(s[i]) + 1 + len(s[i+1]), m)
print(m)

m = 0
for i in range(len(s) - 2):
    m = max(len(s[i]) + 1 + len(s[i+1]) + 1 + len(s[i+2]), m)
print(m)
