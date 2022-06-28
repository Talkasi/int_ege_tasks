a = [int(x) for x in open("17.txt")]
ans = []
sr = sum(x for x in a if x % 2 == 0)/len([x for x in a if x % 2 == 0])
su = 0
p = 0
for i in range(len(a) - 2):
    if max(a[i], a[i+1], a[i+2]) > sr and \
       (sum([a[i], a[i+1], a[i+2]]) - max(a[i], a[i+1], a[i+2]) - min(a[i], a[i+1], a[i+2])) <= sr:
        su += 1
    if len(set([a[i]%3, a[i+1]%3, a[i+2]%3]))==3:
        p+=1
        ans.append(sum([a[i], a[i+1], a[i+2]]))
print(su, p, len(ans), max(ans))

a=[int(x) for x in open('17.txt')]
a1=[int(x) for x in open('17.txt') if int(x)%2==0]
sr=sum(a1)//len(a1)
ans=[]
su  = 0
p = 0
for i in range(len(a)-2):
    if ((a[i]>sr) + (a[i+1]>sr) + (a[i+2]>sr))==1:
        su+=1
    if (a[i]%3)!=(a[i+1]%3) and (a[i]%3)!=(a[i+2]%3) and (a[i+1]%3)!=(a[i+2]%3):
        p+=1
        ans.append(a[i]+a[i+1]+a[i+2])
print(su, p, len(ans),max(ans))

from itertools import *
c= 0
for x in product("VALER'YN", repeat = 10):
    s = ''.join(x)
    if s[0] != "'" and all(s.count(x) == 1 for x in 'AEY'):
        c+=1
print(c)
