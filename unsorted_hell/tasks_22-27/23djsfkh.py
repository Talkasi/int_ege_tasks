def f(n, k):
    if n > k: return 0
    if n == k: return 1
    return f(n+1, k)+f(n+2, k)+f(n+3, k)
print(f(4, 8)*f(8, 15))

