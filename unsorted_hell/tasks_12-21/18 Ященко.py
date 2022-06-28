def f(n, k, c):
    if c > 6: return 0
    if c == 6 and n == k:
        return 1

    if n%2 == 0:
        l = f(n//2, k, c+1)
    else:
        l = 0
    return f(n+1, k, c+1) + l

print(f(8,5,0))
#Да

def f(n, k, c):
    if c > 20: return 0
    if c == 20 and n == k:
        return 1

    if n%2 == 0:
        l = f(n//2, k, c+1)
    else:
        l = 0

    return f(n+1, k, c+1) + l

print(f(1000,62,0))
#Нет

def f(n, k, c, m):
    if c > m: return 0
    if c == m and n == k:
        return 1

    if n%2 == 0:
        l = f(n//2, k, c+1, m)
    else:
        l = 0

    return f(n+1, k, c+1, m) + l

for i in range(1, 10000):
    if f(1000,9,0,i) != 0:
        print(i+1, f(1000,9,0,i))
        break

