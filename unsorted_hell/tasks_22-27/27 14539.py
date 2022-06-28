f = open("27-54b.txt")
n = int(f.readline())
k = [[] for i in range(4)]
ans = []
for i in range(n):
    x = int(f.readline())
    k[x%4].append(x)
#print(k)
for i in range(4):
    k[i] = sorted(k[i])[::-1]
    z = 4 if len(k[i]) > 4 else len(k[i])
    for j in range(z):
        ans.append(k[i][j])
v = 0
#print(ans)
for i in range(len(ans)):
    for j in range(i + 1, len(ans)):
        for k in range(j + 1, len(ans)):
            for m in range(k + 1, len(ans)):
                if (ans[i] + ans[j] + ans[k] + ans[m]) % 4 == 0:
                    #print(ans[i], ans[j], ans[k], ans[m])
                    v = max(v, ans[i] + ans[j] + ans[k] + ans[m])
print(v)
