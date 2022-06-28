a = []
ans = []
for i in open('17-4.txt'):
    a.append(int(i))

for i in range(len(a)):
    if a[i]%16==11 and a[i]%7 == 0 and a[i]%6!= 0\
       and a[i]%13 != 0 and a[i]%19 != 0:
        ans.append(a[i])
print(sum(ans), len(ans))
