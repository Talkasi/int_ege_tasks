
print(7**500 + 7**200 - 7**50)
for x in range(1, 2):
    s = 7**500 + 7**200 - 7**50 - x
    c, k = 0, 0
    while s > 0:
        k+=1
        c+=s%7
        d = s%7
        s = s//7
    print((k- 1)*6, d)

