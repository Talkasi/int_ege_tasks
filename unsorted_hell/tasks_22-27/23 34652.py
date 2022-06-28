def f(n, k, c):
    if n > k or (n == k and c != 7): return 0
    if n == k and c == 7: return 1
    return f(n+1, k, c+1) + f(n+4, k, c+1) + f(n*2, k, c+1)

print(f(3, 27, 0))

s = '1' + '0'*75
while '10' in s or '1' in s:
    if '10' in s:
        s = s.replace("10", '001', 1)
    else:
        s = s.replace("1", '00', 1)
print(s, s.count('0'), 75*2+2)
