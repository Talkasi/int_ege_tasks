def f(n, k):
    if n>k or n==8 or n==15: return 0
    if n == k: return 1
    return f(n+1, k) + f(n+2, k) + f(n*3, k)
print(f(3, 10)*f(10, 22))
