#Task: find maxsum podpos; maxsum%1000 == 0
f = open("27A (54).txt")
n = int(f.readline())
s = [0]
ans = []
for i in range(n):
    x = int(f.readline())
    s = [a+x for a in s] + [x]
    s = {v%1000:v for v in sorted(s)}
    if (0) in s: ans.append(s[(0)])
    s = s.values()
print(max(ans))
