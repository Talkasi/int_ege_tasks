a = [int(x) for x in open("17-5 (1).txt")]
ans = []

for i in range(len(a)- 1):
    if a[i] % 2 == 0 or a[i+1] % 2 == 0:
        ans.append(a[i]+a[i+1])
print(len(ans), max(ans))
