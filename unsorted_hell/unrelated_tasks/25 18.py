def f(n):
    return all(n%i != 0 for i in range(2, int(n**0.5) + 1))

for i in range(55_000_000, 60_000_001):
    n = i
    while n%2 == 0: n = n//2
    k = int(n**0.25)
    if k**4 == n and f(k):
        print(i, k**4)
