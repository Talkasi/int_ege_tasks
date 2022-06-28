def f(n, k):
    if n==12 or n>k: return 0
    if n==k: return 1
    return f(n+1, k) + f(n+3, k) + f(n*2, k)

print(f(3, 8)*f(8, 21))
