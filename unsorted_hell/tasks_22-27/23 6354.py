l = set()
def f(n, c):
    if c == 13: l.add(n)
    if c < 13:
        f(n+3,c+1)
        f(n*2 + 1,c+1)

f(2, 0)
print(l, len(l))

print(hex(2**379 + 2**378 + 2**377)[:10])
s = 2**379 + 2**378 + 2**377
while s > 0:
    x = s % 16
    s = s//16
print(x)
