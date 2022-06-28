c = 0
for s in open('24-s1.txt'):
    for i in range(len(s)-2):
        if s[i]+s[i+2] =='FO':
            c+= 1
            break
print(c)
