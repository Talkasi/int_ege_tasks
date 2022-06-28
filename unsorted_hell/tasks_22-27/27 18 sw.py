f=open('27B (31).txt')
n=int(f.readline())
a=[]
col = 0
ans = []
for i in range(n):
    x= int(f.readline())
    
    if x < 134:

        for i in range(len(a)):
            if x < a[i] and (x+a[i]) <134:
                ans.append(x+a[i])

        a.append(x)

        
print(len(ans))
