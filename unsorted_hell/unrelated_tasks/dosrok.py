#Dosrok
#17
a = [int(x) for x in '1']#open("file.txt")]
#mi4 = min(x for x in a if x%4 == 0)
ans = []
for i in range(len(a) - 1):
    if a[i]%mi4 == 0 and a[i+1]%mi4 == 0:
        ans.append(a[i]+a[i+1])
#print(len(ans), max(ans))

#24
s = '1' #open("file.txt").readline()
s = s.replace('AC', '-')
s = s.replace('AB', '-')
for i in set(s):
    if i != '-':
        s.replace(i, ' ')
s = s.split()
#print(len(max(s, key = len)))

#25
from itertools import product

#alternative
for i,j in product('0123456789', repeat = 2):
    s = '12345' + i + '7' + j +'8'
    s = int(s)
    if s%31 == 0:
        print(s, s//31)
#27a
f = open("test_demo.txt")
n = int(f.readline())
a = [int(x) for x in f]
m = 10**20
for i in range(n):
    s1, s2 = 0, 0
    for j in range(i, n + i):
        s1 += a[i - j] * min(abs(n - abs(i - j)), abs(i - j))
        if i + j >= n: s2 += a[n - j] * min(abs(n - abs(i - j)), abs(i - j))
        else: s2 += a[i + j] * min(abs(n - abs(i - j)), abs(i - j))
    m = min(m, s1, s2)
print(m)



































