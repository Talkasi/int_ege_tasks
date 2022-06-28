a = [int(x) for x in open("17 (10).txt")]
s = [0]*10
for x in a:
    if 100<=abs(x)<1000:
        s[abs(x)//10%10] += 1
print(s) #4
m = 4
ans = []

for i in range(len(a)- 1):
    if (abs(a[i])%10 == m or abs(a[i+1])%10 == m):
        ans.append(a[i]+a[i+1])
print(len(ans), max(ans))
