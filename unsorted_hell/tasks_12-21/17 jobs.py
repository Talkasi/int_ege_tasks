s = open('24 (41).txt').readline()
print(len(s))
c = ''
m = ''
for i in range(len(s)):
    c += s[i]
    if s[i] == '.':
        c = ''
    while sum(c.count(x) for x in 'AEIOUY') > 7:
        c = c[1:]

    m = max(m, c, key = len)
print(m, len(m))



f=open('24 (39).txt').readline()
s=''
m=''
for i in range(len(f)):
    s+=f[i]
    while s.count('A')>1:
        s=s[1:]
    m = max(m, s, key = len)
print(m, len(m))


f=open('24 (39).txt').readline()
s=''
m=0
for i in range(len(f)):
    s+=f[i]
    if s.count('A')<=1:
        m=max(m,len(s))
    else:
        while s.count('A')>1:
            s=s[1:]
        
print(m)
