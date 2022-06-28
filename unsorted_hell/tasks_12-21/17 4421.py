a = []
for i in open('17-202.txt'):
    a.append(int(i))
ans = []
for i in range(len(a) - 2):
    if not (a[i]%10==5 and 99<a[i]<1000) and \
       not (a[i+2]%10==5 and 99<a[i+2]<1000) and \
       (a[i+1]%10==5 and 99<a[i+1]<1000):
        ans.append(a[i]+a[i+1]+a[i+2])
print(len(ans), max(ans))
