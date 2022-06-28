for i in range(1001, 100000):
    n = bin(i)[2:]
    n = n[::-1]
    while n[0] == '0': n = n[1:]
    n = int(n, 2)
    if n == 29:
        print(i)
        break
for i in range(1, 100000):
    d = i
    n = 2
    s = 0
    while s <= 365:
        s = s+d
        n = n+5
    if n == 67:
        print(i)
        break





s = "3" + "5" *57

while '25' in s or '355' in s or '4555' in s:
    if '25' in s: s = s.replace("25", "3", 1)
    if '355' in s: s = s.replace("355", "4", 1)
    if "4555" in s: s = s.replace("4555", "2", 1)
print(s)


c = 0
s = 81**15 + 3 **22 - 27
while s > 0:
    if s % 9 == 8: c+= 1
    s = s//9
print(c)





for a in range(1, 1000000):
    if all((x&13 == 0) <= ((x&40!=0) <= (x&a != 0)) for x in range(1, 100000)):
        print(a)
        break
def f(n):
    if n< 2: return 1
    if n % 3 == 0: return f(n//3) - 1
    return f(n - 1) + 17

for i in range(1, 100000):
    if f(i) == 110:
        print(i)
        break

a = [int(x) for x in open("17-10.txt")]
ans = []

for i in range(len(a)):
    if 99< (a[i] + a[i+1])<1000 and (a[i] + a[i+1])%10 > (a[i] + a[i+1])//10%10:
        ans.append(a[i] + a[i+1])
print(len(ans), min(ans))





































































