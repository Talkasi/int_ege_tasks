for i in range(185, 200):
    s = i*'1'
    while '1111' in s:
        s = s.replace('1111', '2', 1)
        s = s.replace('22', '11', 1)
    print(s)

s = 25 ** 94 + 5 ** 216 - 125
c = 0
while s > 0:
    if s % 5 == 4:
        c+=1
    s = s//5
print(c)

def f(n, k):
    if n > k or n == 15: return 0
    if n == k: return 1
    return f(n+1, k) + f(n+3, k)
print(f(2, 10)*f(10, 20))
