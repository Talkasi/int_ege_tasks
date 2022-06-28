def f(x):
    k=0
    x1=x
    p = 0
    while x>9:
        if (x//9)%9>=x%9:
            k += x % 9
            p = x % 9
            x=x//9
        else:
            k=0
            break
    if k != 0 and int(str(x)[0]) >= p:
        k += int(str(x)[0])
    else:
        k = 0
    return str(x1),k

##for i in range(1,100):
print(int("7644321", 9),f(int("7644321", 9)))
for x in range(3045802,10**8):
    d,b=f(x)
    if len(d)>0 and b>0:
        if d[0]=='3' and d[2]=='4' and d[3]=='5' and d[4]=='8' and d[-1]=='3':
            print(x,b)
