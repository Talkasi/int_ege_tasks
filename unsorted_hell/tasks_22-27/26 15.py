f = open("26/26-15.txt")
n = int(f.readline())
w = ['0']*2_000_000

for i in range(n):
    a, s = map(int, f.readline().split())
    for i in range(a-1, a + s - 1):
        w[i] = '1'

c = 0
for i in range(n):
    if w[i] == '0' and w[i+1] == '1':
        c+=1

print(c, w.count('1'))

