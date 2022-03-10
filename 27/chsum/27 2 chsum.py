#Task: choose maxssum, maxsum%10!=5
f = open('27-A (1).txt')
n = int(f.readline())
s = [0]

for i in range(n):
    pairs = [int(x) for x in f.readline().split()]
    s = [a+b for a in s for b in pairs]
    s = {x%10:x for x in sorted(s)}.values()
print(max(x for x in s if x%10!=5))
