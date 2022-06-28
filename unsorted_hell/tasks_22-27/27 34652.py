f = open("27-52a.txt")
n = int(f.readline())
ost = [[] for i in range(3)]
ans = []
for i in range(n):
    x = int(f.readline())
    ost[x%3].append(x)
    
for i in range(3):
    ost[i] = sorted(ost[i])[::-1]
    end = 3 if len(ost[i]) >= 3 else len(ost[i])
    for j in range(end):
        ans.append(ost[i][j])
v = 0
#print(ans)
for i in range(len(ans)):
    for j in range(i+1, len(ans)):
        for k in range(j+1, len(ans)):
            if (ans[i]+ans[j]+ans[k])%3 == 0:
                v = max(v, ans[i]+ans[j]+ans[k])
print(v)
