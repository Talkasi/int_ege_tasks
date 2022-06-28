a = [int(x) for x in open('24-j6.txt').readline()]
t=0
k,m = 1,0
for i in range(1,len(a)):
    if a[i-1]<a[i]:
        k+=1
    else:
        if k==5:
            t+=1
        k = 1
print(t)
