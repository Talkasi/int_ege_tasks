def f(n):
    if n == 0: return 8
    if n%3 == 0:return 5+f(n//3)
    return f(n//3)
c = 0
for i in range(9, 100_000_001):
    if i%9 == 0 and i % 27 != 0:
        if f(i) == 18:
            #print(i, f(i))
            #input()
            c += 1
print(c)
