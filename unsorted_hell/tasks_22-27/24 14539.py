s = open("24-4.txt").readline()
#s = 'ASDFabcd016789GfL'
c = s[0]
m = ''
for i in range(len(s) - 1):
    if s[i] < s[i+1]:
        c += s[i+1]
    else:
        m = max(m, c, key = len)
        c = s[i+1]
m = max(m, c, key = len)
print(m, len(m))

s = 25**94 + 5**216 - 125
c = 0
while s >0:
    if s %5 == 4: c+=1
    s = s//5
print(c)

for a in range(1, 10000000):
    if all((x*y < 4*a) or (x >= 21) or (x < 4*y) for x in range(1, 10000) for y in range(1, 10000)):
        print(a)
        break
    
