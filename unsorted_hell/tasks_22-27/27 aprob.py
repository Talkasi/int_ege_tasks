print("Var 1")
f = open("27_A (7).txt")
n = int(f.readline())
m, s = 0, 0
stat = [10**20] * 67

for i in range(n):
    x = int(f.readline())
    s += x
    if s % 67 == 0: m = max(m, s)
    m = max(m, s - stat[ s % 67 ])

    stat[ s % 67 ] = min(stat[ s % 67 ], s)
print(m)

print("Var 2")
f = open("27_A (7).txt")
n = int(f.readline())
m, s = 0, [0]
stat = [10**20] * 67

for i in range(n):
    x = int(f.readline())
    s = [a + x for a in s] + [x]
    s = {a%67:a for a in sorted(s)}.values()
print(max(x for x in s if x%67 == 0))
