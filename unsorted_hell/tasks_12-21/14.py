print(bin(8**740 - 2**900 + 7)[2:].count('0'))

s = 8**740 - 2**900 + 7
c = 0
while s>0:
    if s%2 == 0:
        c+=1
    s = s//2
print(c)
