'''s = open('24-1.txt').readline()
m = 0
prev_i = 10**20
for i in range(1,len(s)-1):
    if ord(s[i-1]) < ord(s[i]) > ord(s[i+1]):
        m = max(i - prev_i, m)
        prev_i = i

print(m)'''
k = 0
for s in open('24-200.txt'):
    s = s.strip()
    if len(s)>6:
        if s[:5]=='195.2' and s[-3:]=='.14':
            k += 1

print(k)

k=0
for s in open('24-200.txt'):
    if len(s)>6:
        if s[0]+s[1]+s[2]+s[3]+s[4]=='195.2' and s[-4]+s[-3]+s[-2]=='.14':
            k+=1

print(k)
