#Task: choose two in three, maxsum%4==0
f = open('27-A (3).txt')
n = int(f.readline())
s = [0]

for i in range(n):
    tr = [ int(x) for x in f.readline().split() ]
    pairs = [tr[0]+tr[1], tr[0]+tr[2], tr[1]+tr[2]]
    s = [a+b for a in s for b in pairs]
    s = {x%4:x for x in sorted(s)}.values()
print(max(x for x in s if x%4==0))
    
