f = open("17.txt")
a = [int(x) for x in f]
m11 = max(x for x in a if x%11 == 0)
ans = []
for i in range(len(a) - 1):
    if (abs(a[i]) % 11 == 0 or abs(a[i + 1]) % 11 == 0) and \
       (a[i] + a[i+1]) <= m11:
        ans.append(a[i] + a[i+1])
print(len(ans), max(ans))
