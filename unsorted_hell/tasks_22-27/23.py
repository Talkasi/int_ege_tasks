def f(n, k):
    if n > k or n == 15: return 0
    if n == k: return 1
    return f(n + 1, k) + f(n * 2, k)

print(f(2, 12) * f(12, 32))
