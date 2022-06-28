def f(n, k, co):
    if co > 1: return 0
    if n > k: return 0
    if n == k and co == 1: return 1
    if n == k and co != 1: return 0
    return f(n + 1, k, co) + f(n + 2, k, co) + f(n * 2, k, co + 1)

print(f(2, 12, 0))
