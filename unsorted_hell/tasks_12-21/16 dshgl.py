def f(n):
    if n < 2: return n
    if n % 2 == 0: return f(n//2) + 1
    return f(n*3 + 1) + 1
c = 0

for i in range(1, 100001):
    if f(i) == 16: c+=1
print(c)
