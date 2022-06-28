f = open("26-52 (2).txt")
n = int(f.readline())
a = sorted(int(x) for x in f)
ans = [] #не более
for i in range(101):
    for j in range(i):
        if (a[i] + a[j]) % 10 == 0:
            ans.append((a[i] + a[j])/2)

for i in range(101, len(a)):
    for j in range(1, 102):
        if (a[i] + a[i - j]) % 10 == 0:
            ans.append((a[i] + a[i - j])/2)

print(len(ans), min(ans))
            
            
