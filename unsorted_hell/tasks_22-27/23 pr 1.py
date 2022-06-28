def f(n, k):
    if n > k: return 0
    if n == k: return 1
    if n < k:
        return f(n+2, k) + f(n*2, k)
print(f(1, 18)*f(18, 52))
