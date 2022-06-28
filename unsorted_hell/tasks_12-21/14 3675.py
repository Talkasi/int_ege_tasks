s = 10000 + 625 **25 + 5**100
c = 0
while s >0:
    if s%15 ==12:
        c+=1
    s = s//15
print(c)
