def f(n, k):
    if n > k: return 0
    if n == k: return 1
    return f(n - 1, k) + f(n//2, k)
print(f(int('110111', 2), int('110', 2)))
