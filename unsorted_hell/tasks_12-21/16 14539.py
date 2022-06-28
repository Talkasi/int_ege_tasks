def f(n):
    if n < 2: return 1
    if n % 3 == 0: return f(n//3) + 1
    return f(n - 2) + 5
c = 0
for n in range(1, 100_001):
    if f(n) == 55:
        c+=1
print(c)

a = [int(x) for x in open('17-199.txt')]
ans = []

for i in range(len(a) - 2):
    if (not(a[i] > 0 and abs(a[i]) % 2 != 0 and 100 <= abs(a[i]) < 1000))\
       and (a[i+1] > 0 and abs(a[i+1]) % 2 != 0 and 100 <= abs(a[i+1]) < 1000)\
       and (not(a[i+2] > 0 and abs(a[i+2]) % 2 != 0 and 100 <= abs(a[i+2]) < 1000)):
        ans.append(a[i]+a[i+1]+a[i+2])
print(len(ans), max(ans))
