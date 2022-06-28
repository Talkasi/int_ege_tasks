a = []
ans = []
for i in open('17-3.txt'):
    a.append(int(i))

for i in range(len(a) - 1):
    if (a[i]%4 == 0 and a[i+1]%11 == 0 and a[i+1]%2 != 0) or \
       (a[i+1]%4 == 0 and a[i]%11 == 0 and a[i]%2 != 0):
        ans.append(a[i]+a[i+1])
print(len(ans), max(ans))
