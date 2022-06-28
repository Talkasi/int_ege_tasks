a = [int(x) for x in open("17 (12).txt")]
m = min(x for x in a if x%21 == 0)
ans = []
for i in range(len(a) - 1):
    if a[i]%m == 0 or a[i+1]%m == 0:
        ans.append(a[i]+a[i+1])
print(len(ans), max(ans))
