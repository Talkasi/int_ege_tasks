f = open('test (2).txt')
n = int(f.readline())
a = sorted(int(f.readline()) for i in range(n))
s = sum(a)
ans, previous = [], []
for i in range(n):
    if sum(previous) < a[i]:
        ans.append(a[i])
    previous.append(a[i])
print(len(ans), max(ans), ans)
    
