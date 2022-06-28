def f(x):
    d=set()
    for i in range(2,int(x**0.5)+1):
        if x%i==0:
            if i%2 == 0:
                d.add(i)
            if (x//i)%2 == 0:
                d.add(x//i)

    return sorted(d)
k = 0
for x in range(99_999_998,99999000,-2):
    d=f(x)
    if len(d)>4 and d[-5]>0:
        print(x,d[-5],len(d))
        k += 1
    if k == 5: break
