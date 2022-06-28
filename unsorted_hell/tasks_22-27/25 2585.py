def f(n):
    if not any(n%i == 0 for i in range(2, int(n**0.5) + 1)):
        return 1
    else:
        return 0

c = 0
for i in range(2532000, 2532161):
    if f(i):
        c += 1
        print(c, i)
    if c == 5:
        break
