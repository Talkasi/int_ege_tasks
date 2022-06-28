for i in range(1, 10000000):
    x = i
    l = 0
    m = 0
    while x > 0:
        l += 1
        if x % 2 == 0:
            m = m + (x % 10) //2
        x = x // 10
    if l == 3 and m == 7:
        print(i)
        break

def f(n, k):
    if n > k: return 0
    if n == k: return 1
    if n%2 != 0:
        return f(n+1, k)
    return f(n+1, k) + f(n * 1.5, k)
print(f(2, 22))
