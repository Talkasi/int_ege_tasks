f = open('test.txt')
n = int(f.readline())
a = [int(x) for x in f]
ans = []
for i in range(n):
    for j in range(i + 1, n):
        if (a[i] + a[j])%3 == 0:
            ans.append(a[i] + a[j])
print(ans, len(ans))
