def f(n, k):
    if n == k: return 1
    if n > k: return 0
    return f(n + 1, k) + f(n * 2, k) + f(n * 3, k)
print(f(2, 7) * f(7, 28))
