f = open("17-275.txt")
a = [int(x) for x in f]
for i in range(len(a) - 1):
    if (a[i]+a[i+1])%11 == 0:
        ans.append(a[i]+a[i+1])
print(len(ans), max(ans))
