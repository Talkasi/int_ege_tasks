a = [x for x in open("17 (2).txt")]
sr = sum(a)/len(a)
ans = []
for i in range(len(a) - 2):
    if ((a[i]>sr) + (a[i+1]>sr) + (a[i+2]>sr)) >= 2:
        ans.append(a[i] + a[i+1] + a[i+2])

print(len(ans), max(ans))
