s = 3**72 + 6*3**50 - 7*3**26 + 2*3**15 + 155
c = set()
while s >0:
    c.add(s%9)
    s = s//9
print(len(c))
