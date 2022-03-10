#Task: maxsum podpos, maxsum%69==0. len_maxssum - ?
f = open("27_A (6).txt")
n = int(f.readline())
s = [ [0,0] ]
ans = []
for i in range(n):
    x = int(f.readline())
    s = [[a+x, b+1] for a,b in s] + [ [x,1] ]
    s = {a[0]%69:a for a in sorted(s)}
    if (0) in s: ans.append(s[(0)])
    s = s.values()
ans.sort()
print(ans[-10:])
    
