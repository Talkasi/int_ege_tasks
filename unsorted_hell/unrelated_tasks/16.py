def f(n):
    if n <= 1: return 1
    if n > 1 and n % 2 == 0: return 3 * n + f(n - 1)
    return 2 * f(n - 3)
print(f(30))