f = open("26 (16).txt")
s, n = map(int, f.readline().split())
box = []
a = sorted(int(x) for x in f)

for i in range(n//2 + 1):
    if sum(box) + a[n - i - 1] + a[i] <= s:
        box.append( a[n - i - 1] )
        box.append( a[i] )
        a[n-i-1] = 0
        a[i] = 0

a = sorted(x for x in a if x != 0)
if sum(box) + a[-1] <= s:
    box.append( a.pop(-1) )
print(len(box), box[-1])
    

