s = 6*(512**180) + 7*(64**181) + 3*(8**184) + 5*(8**125) - 65
c = 0
while s > 0:
    if s % 64 == 0:
        c+=1
    s = s//64
print(c)
