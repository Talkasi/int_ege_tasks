mo= 0
for i in range(1, 10000):
    x = i
    l, m = 0, 0
    while x > 0:
        l += 1
        if x % 2 == 0:
            m = m + (x%10)//2
        x = x//10
    if l == 3 and m == 7:
        mo = max(mo, i)
print(mo)
