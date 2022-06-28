#Task: choose minsum, minsum%5!=0
f = open('27-A (2).txt')
n = int(f.readline())
s = [0]

for i in range(n):
    pairs = [ int(x) for x in f.readline().split() ]
    s = [a+b for a in s for b in pairs]
    s = {x%5:x for x in sorted(s)[::-1]}.values()
print(min(x for x in s if x%5!=0))
