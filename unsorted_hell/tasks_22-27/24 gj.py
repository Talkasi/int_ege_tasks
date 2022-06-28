a=open('24-153.txt').readline()
s=''
m=0

for i in range(len(a)-1):
    if a[i]=='A':
        s+=a[i]
        if a[i+1]!='F':
            for j in range(i+1,len(a)):
                if a[j]!='F':
                    s+=a[j]
                else:
                    s+=a[j]
                    break
            m=max(m,len(s))
            s=''
                
    
print(m)
