#Task: maxsum podpos, kol5 = kol7
f = open("27-96b.txt")
n = int(f.readline())
ans = []
s = [ [0, 0, 0] ]
m = 0
k7, k5 = 0, 0
for i in range(n):
    x = int(f.readline())
    k7 += (x%7 == 0)
    k5 += (x%5 == 0)
    m = min(k7, k5)
    s = [[a+x, k5 + int(x%5 == 0), k7 + int(x%7 == 0)] for a, k5, k7 in s] + [ [x, int(x%5 == 0), int(x%7 == 0)] ]
    s = {(k5, k7):[a, k5, k7] for a, k5, k7 in sorted(s)}
    if (m, m) in s:
        ans.append(s[(m,m)])
    s = s.values()
    #s = sorted(s)[-1000:]
    if i==20000: print(len(s))
    input()
print(max(ans))

