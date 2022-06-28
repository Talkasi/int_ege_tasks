f = open("27_B (5).txt")
n = int(f.readline())
s = [ [0,0] ]
ans = []
for i in range(n):
    x = int(f.readline())
    s = [[a+x, b+(x%5==0)] for a,b in s] + [ [x,int(x%5==0)] ]
    s = {v[1]%3:v for v in sorted(s)}
    if (0) in s: ans.append(s[(0)])
    s = s.values()
ans.sort()
print(ans[-10:])
