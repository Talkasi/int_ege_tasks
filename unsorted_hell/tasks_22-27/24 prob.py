s = open("24 (30).txt").readline().strip()

m = ''
c = ''
for i in range(len(s)):
    c += s[i]
    while 'PR' in c and 'ST' in c:
        c = c[1:]
    m = max(m, c, key= len)
print(len(m), 'PR' in m, 'ST' in m)

    
            
