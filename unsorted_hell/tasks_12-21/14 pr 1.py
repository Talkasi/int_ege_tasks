s = 7*(512**1912) + 6*(64**1954) - 5*(8**1991) - 4*(8**1980) - 2022
c = 0
while s >0:
    if s % 8 == 7: c+=1
    s = s//8
print(c)
