from itertools import product
c = 0

for i in product('0123456789', repeat = 5):
    s = ''.join(i)
    if s[0] != '0' and s[-1] != '3' and s[-1] != '4' and s[-1] != '7' and \
       not(any(x+x+x in s for x in '0123456789')):
        #print(s)
        c += 1
print(c)
