#Task: podpos, sumpodpos%17==0; maxssum - ?
f = open('27_A (4).txt')
n = int(f.readline())
s = [0]
ans = []
for i in range(n):
    x = int(f.readline())
    s = [x] + s + [a+x for a in s]
    s = {v%17:v for v in sorted(s)}
    if (0) in s: ans.append(s[(0)])
    s = list(s.values())
print(max(ans))
    
