def f(x):
    d=set()
    d1=set()
    d3=set()
    for i in range(1,int(x**0.5)):
        if x%i==0:
            if i%2==0:
                d.add(i)
            if i%2!=0:
                d1.add(i)
            if (x//i)%2==0:
                d.add(x//i)
            if (x//i)%2!=0:
                d1.add(x//i)
            if (x//i)>1000:
                d3.add(x//i)
            if i>1000:
                d3.add(i)
    if len(d)==len(d1) and len(d) >= 70 and len(d1)>=70:
        return sorted(d3)
    else: return 0
                

for i in range(326496,649633):
    d=f(i)
    if d!=0: print(i,d[0])
