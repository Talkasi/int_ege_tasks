s = open("24-j2.txt").readline()
m = ''
for a in 'FAIL':
    c = s
    for x in 'FAIL':
        if x != a:
            c = c.replace(x, ' ')
    c = c.split()
    m = max(max(c), m, key = len)
print(len(m))

a = open('24-j2.txt').readline()
k=1
m=0
for i in range(len(a)-1):
    if s[i]==s[i+1]:
        k+=1
        m=max(m,k)
    else:
        k=1
print(m)

