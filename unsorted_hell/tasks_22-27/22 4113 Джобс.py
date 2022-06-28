c = 0
for i in range(1, 1_000_000):
    x = i
    x = (x - x % 8) * 10 #сбрасывается до наибольшего кратного 8 и умножается на 10
    a = 1
    b = 0
    while x > 0:
        if x % 2 != 0:
            a = a * (x % 4)
        else:
            b = b + (x % 4)
        x = x// 8
        if b > 5 or a > 9: break
    if a == 9 and b == 5:
        c+=1
print(c)

c = 0
def f(n):
    return all(n%i != 0 for i in range(2, int(n**0.5) + 1))
for i in range(2, 3577001):
    if f(i):
        c+=1
print(c)

s = open("24-3.txt").readline()
c, m = s[0], ''
for i in range(len(s) - 1):
    if s[i] < s[i+1]:
        c+= s[i+1]
    else:
        m = max(c, m, key = len)
        c = s[i+1]
m = max(c, m, key = len)
print(len(m), m)






