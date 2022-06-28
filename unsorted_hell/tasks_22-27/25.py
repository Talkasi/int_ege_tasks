def f(x):
    return x>1 and all(x%i!=0 for i in range(2,int(x**0.5)+1))

def g(x):
    d=set()
    for i in range(2,int(x**0.5)+1):
        if x%i==0:
            d.add(i)
            d.add(x//i)
    if len(d)==2:
        return(sorted(d))
    if len(d)!=2:
        return 0,0
c=0
ans=[]
for x in range(237981,309877):
    a,b=g(x)
    if f(a) and f(b) and a*b==x and a%10==b%10:
        c+=1
        ans.append(x)
print(c, max(ans))
