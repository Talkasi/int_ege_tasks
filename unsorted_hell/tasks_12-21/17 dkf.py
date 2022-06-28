f = open("17-1.txt")
a = [int(x) for x in f]
sr = sum(a)/len(a)
ans = []
for i in range(len(a) - 2):
    if (a[i] < sr or a[i+1] < sr or a[i+2] < sr) and \
       (a[i] %3 == 0 or a[i+1] % 3 == 0 or a[i+2] % 3 == 0):
        ans.append(a[i] + a[i+1] + a[i+2])
print(len(ans), max(ans))
