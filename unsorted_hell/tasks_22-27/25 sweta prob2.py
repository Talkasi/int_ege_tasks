def f(x):
    d=set()
    l=0
    for i in range(2,int(x**0.5)+1):
        if x%i==0 and i%2==0:
            d.add(i)
            l+=1
            if (x//i)%2==0:
                d.add(x//i)
                l+=1
    s = [x for x in sorted(d)]
    if l==6: return s[-6]
    else: return 0
k=0
for x in range(1,100000000):
    d=f(x)
    if d!=0:
        print(x,d)
        k+=1
    if k==5: break
