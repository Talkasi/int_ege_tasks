a = open("24.txt").readline().strip()
s, m = '', ''
for i in range(len(a)):
    s += a[i]
    while s.count('D') + s.count('C') > 3: s = s[1:]
    m = max(m, s, key = len)
print(m, len(m))

c, l = [], []
for n in range(10):
    for m in range(13):
        for k in range(26):
            if 3*n+2*k+m==25:
                if n + m + k == 9: c.append((n, m, k))
                if n + m + k < 9: l.append(m+n+k)
print(c, l)
                
a=open('24.txt').readline()
k=0
m=0
s=''
mx=0
l=10**6
for i in range(len(a)):
    m+=1
    if a[i]=='C' or a[i]=='D':
        k+=1
        l=min(l,m+2)
    s=s+a[i]
    if k==4:
        k-=1
        m=0
        #print(s)
        s=s[l:]
        l=10**6
        if s.count('D') + s.count('C') > 3:
            print("error:", s)
    mx=max(mx,len(s))   
print(mx)
