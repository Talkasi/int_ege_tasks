for i in range(1, 1000000000000000000):
    x = i
    a = 0
    b = 1
    while x > 0:
        a = a+1
        b = b*(x%1000)
        x = x//1000
    if a == 2 and b == 11:
        print(i)
        break
def p(n):
    while any(n%x == 0 for x in range(2, int(n**0.5) + 1)):
        n += 1
    return n

def f(n, k):
    if n > k or n == 33: return 0
    if n == k: return 1
    s = p(n) if any(n%x == 0 for x in range(2, int(n**0.5) + 1)) else p(n+1)
    return f(n+2, k) + f(s, k)
print(f(2, 14) * f(14, 45))
