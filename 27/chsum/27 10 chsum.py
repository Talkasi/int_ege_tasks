#Task: minsum podpos, minsum%2077 == 0, len - ?
f = open("27A (56).txt")
n = int(f.readline())
s = [ [0,0] ]
ans = []
for i in range(n):
    x = int(f.readline())
    s = [[a+x, b+1] for a,b in s] + [ [x,1] ]
    s = {x[0]%2077:x for x in sorted(s)[::-1]}
    if (0) in s: ans.append(s[(0)])
    s = s.values()
ans = sorted(ans)[::-1]
print(ans[-10:])
