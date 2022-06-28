def f(n, k):
    if n > k: return 0
    if n == k: return 1
    return f(n+1, k) + f(n+2, k)
print(f(11,17)*f(17, 29) + f(11, 23)*f(23, 29) - f(11, 17)*f(17, 23)*f(23, 29))
