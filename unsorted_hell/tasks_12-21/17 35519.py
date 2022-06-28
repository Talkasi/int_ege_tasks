a = [int(x) for x in open("17-4 (2).txt")]
ans = []

for i in range(len(a)):
    if str(a[i]).count('0') >= 2 and a[i] % 7 == 0:
        ans.append(a[i])
print(max(ans), len(ans))

def f(n):
    if n < 2: return 1
    if n >= 2 and n%2 == 0:
        return f(n//2) + 1
    if n >= 2 and n%2 != 0:
        return f(n - 3) + 3

for i in range(1, 10000000000):
    if f(i) == 31:
        print(i)
        break
