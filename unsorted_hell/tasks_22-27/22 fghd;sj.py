print(12*7+12*11+12*11*10/3/2)

def f(n, k, m, mm):
    m+=1
    if n == k and m == mm: return 1
    if n < k: return f(n+2, k, m, mm) + f(n*2, k, m, mm)
    return 0

for i in range(1, 100000):
    a = f(1, 100, 0, i)
    if a != 0:
        print(i)
        break
