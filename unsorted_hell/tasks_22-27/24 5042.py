a = open('24-197.txt').readline()
k, i, m = 0, 2, 0
while i + 2 < len(a):
    if (a[i]=='X' and a[i+2]=='X') or (a[i]=='Y' and a[i+2]=='Y'):
        k += 1
        i += 3
    else:
        m = max(m, k)
        k = 0
        i += 1
m = max(m, k)
print(m)

def f(n, k, c):
    if n == k and c == 6: return 1
    if n > k or n == k and c != 6: return 0
    return f(n*2, k, c+1) + f(n+1, k, c+1) + f(n+2, k, c+1)
print(f(1, 20, 0))

a = [int(x) for x in open('17-7.txt')]
ans = []

for i in range(len(a) - 2):
    if a[i]%3 == 2 or a[i+1] % 3 == 2 or a[i+2] % 3 == 2:
        ans.append(min(a[i], a[i+1], a[i+2]))
print(len(ans), sum(ans))

for i in range(10000000, 1, -1):
    x = i
    L, M = 0, 0
    while x > 12:
        L = L + 1
        x = x // 4
        M = x
    if L > M:
        L, M = M, L
    if L == 3 and M == 7:
        print(i)
        break

