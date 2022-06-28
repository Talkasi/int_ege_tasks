n = 1
s = 0
while n <= 300:
    s = s + 30
    n = n * 5
print(s)


n = bin(120)[2:]
while len(n) < 8: n = '0' + n
print(n, bin(120))
n = n.replace('0', '-')
n = n.replace('1', '0')
n = n.replace('-', '1')
print(n)

n = int(n, 2) + 1
print(n)
    
k = 0, 1
for x in k:
    for y in k:
        for z in k:
            for w in k:
                if ((w <= y) and ((x <= z) == (y<=x))):
                    print(x, y, z, w)

for i in range(1,2):
    x=120
    x=bin(x)[2:]
    print(x)
    x='0'*(8-len(str(x))) + x
    print(x)
    x=x.replace('0','A').replace('1','0').replace('A','1')
    print(x)
    x=int(x,2)
    print(x)
