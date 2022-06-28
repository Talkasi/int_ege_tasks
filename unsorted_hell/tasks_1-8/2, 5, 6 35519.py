'''k = 0, 1
for x in k:
    for y in k:
        for z in k:
            if  ((not(x)) and z) or (not(x or y or z)):
                print(x, y, z)

for i in range(1, 100000):
    n = bin(i)[2:]
    n = n + str(sum(int(x) for x in n)%2)
    n = n + str(sum(int(x) for x in n)%2)
    if int(n, 2) > 170:
        print(i)
        break

x = 23
fl = 1
while x < 100:
    if x % 2 == 0:
        x = x//2
    else:
        x = 3*x + 1
print(x)
    '''
for i in range(1, 1000000):
    x = i
    fl = 1
    while x < 100:
        if x % 2 == 0:
            x = x//2
        else:
            x = 3*x + 1
        if x <= 1:
            fl = 0
            break
        #print(x)
        #input()
    if fl == 1:
        print(i)
        input()
