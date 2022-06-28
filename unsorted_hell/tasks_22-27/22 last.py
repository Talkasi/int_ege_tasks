s = 2197**50 - 169 ** 35 - 26
c = 0
while s > 0:
    if s % 13 == 12: c+= 1
    s = s//13
print(c)

for a in range(1, 1000000):
    if all(((x%15 != 0) or (x % 28 != 0) or (x%a == 0)) and (a > 70) \
           for x in range(1, 1000000)):
        print(a)
        break

def f(n):
    if n == 1: return 1
    if n % 2 == 0 and n > 1: return n*f(n - 1)
    if n > 1 and n % 2 == 1: return 1 + f(n - 2)

print(f(84))

