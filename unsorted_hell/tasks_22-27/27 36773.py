f = open("27-3b.txt")
n = int(f.readline())
s = [0]
for i in range(n):
    pa = [int(x) for x in f.readline().split()]
    s = [a+p for a in s for p in pa]
    s = {a%3:a for a in sorted(s)[::-1]}.values()
print([x for x in s if x%3 == 0])
