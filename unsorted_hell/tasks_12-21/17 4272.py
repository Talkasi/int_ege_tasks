a = []
ans = []
for i in open('17-1.txt'):
    a.append(int(i))

for i in range(len(a) - 1):
    if a[i] < a[i+1]:
        ans.append(a[i+1] - a[i])
print(len(ans), min(ans))
