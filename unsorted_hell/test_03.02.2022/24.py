c = 0
v = 0
for s in open("24 (29).txt"):
    for i in range(len(s) - 3):
        if s[i]+s[i+2]+s[i+3] == 'ZRO':
            c += 1
            break
    for i in set(s):
        if ('Z' + i +'RO') in s:
            v += 1
            break
print(c, v)
