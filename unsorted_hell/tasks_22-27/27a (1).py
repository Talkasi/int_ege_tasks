'''
f = open('27-B (5).txt')
n = int(f.readline())
s = [[0,0,0]]
su = 0
for i in range(n):
    t = [int(x) for x in f.readline().split()]
    su += sum(t)
    to = [[t[0], t[1]], [t[1], t[2]], [t[2], t[0]], [t[1], t[0]], [t[2], t[1]], [t[0], t[2]]]

    s = [[x[0]+i[0], x[1] + i[1], x[2] + sum(t) - sum(i)]  for x in s for i in to]
    s = {(x[0]%2, x[1]%2, x[2]%2): x for x in sorted(s)}
    if i != n - 1: s = s.values()
print(s) 

f = open('27a (60).txt')
n = int(f.readline())
s = [0]
for i in range(n):
    p = [int(x) for x in f.readline().split()]
    s = [x+a for x in s for a in p]
    s = {x%10:x for x in sorted(s)}.values()
print(max(x for x in s if x%10 == 8))
'''

f = open("27_A (10).txt")
n = int(f.readline())
s = [0]

for i in range(n):
    t = [int(x) for x in f.readline().split()]
    s = [x+a for x in s for a in t]
    s = {x%117:x for x in sorted(s)[::-1]}.values()

print(min(x for x in s if x % 117 != 11))





































