def f(n):
    if n <= 5: return n
    if n > 5 and n % 4 == 0: return n + f(n//2 - 1)
    return n + f(n + 2)

for n in range(1, 10000):
    try:
        print(f(n), n)
    except:
        ...

for i in range(1, 10000):
    x = i
    l = 0
    m = 0
    while x > 0:
        l += 1
        if x % 2 == 0:
            m = m + (x%10)//2
        x = x//10
    if l == 3 and m == 7:
        print(i)
