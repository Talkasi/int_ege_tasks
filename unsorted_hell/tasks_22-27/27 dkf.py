f = open("test -.txt")
n = int(f.readline())
s = [0]
a = 0
for i in range(n):
    pair = [int(x) for x in f.readline().split()]
    a = a + sum(pair)
    s = [x + p for x in s for p in pair]
    s = {abs(x - (a - x)) % 5: x for x in sorted(s)}.values()
print(max(abs(x - (a - x)) for x in s if (abs(x - (a - x)))%5 == 0))
