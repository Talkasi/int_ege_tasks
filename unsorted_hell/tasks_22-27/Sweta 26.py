f = open('26-66.txt')
N,K=map(int,f.readline().split())
d=24*3600*1000
a=[0]*(d+1)
st=K
end=K+d
for i in range(N):
    n,k=map(int,f.readline().split())
    if (k>st or k==0) and (n<end or n==0):
        if n<st or n==0: n=st
        if k>end or k==0: k=end
        a[n-st]+=1
        a[k-st]-=1
        
t=0
mx=0
c=0
for i in range(d+1):
    t+=a[i]
    if t>mx: mx,c=t,0
    if t==mx: c+=1
print(mx,c)
