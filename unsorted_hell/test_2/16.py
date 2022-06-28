def f(n):
    if n <= 18: return n + 3
    if n%3 == 0: return n//3 * f(n//3) + n - 12
    return f(n - 1) + n*n + 5
c = 0
for i in range(1, 801):
    s = str(f(i))
    if sum(s.count(j) for j in '13579') == 0:
        c += 1
print(c)
