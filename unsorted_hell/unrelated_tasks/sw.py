f=open('26-15.txt')
n=int(f.readline())
a=[0]*2_000_001
for i in range(n):
    st,ln=map(int,f.readline().split())
    a[st]+=1
    a[st+ln]-=1
k=0
st= -1
end=0
C,L=0,0
for i in range(2_000_001):
    k1=k
    k+=a[i]
    if k>0 and st==-1: st=i
    if k==0 and k1>0:
        end = i
        C+=1
        L+=end - st
        st, end=-1,0
print(C,L)
