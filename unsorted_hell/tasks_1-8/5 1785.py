print('1')
input()
for i in range(1, 100):
    n = bin(i)[2:]
    if i%2==0: n+='01'
    else: n+='10'
    n = int(n, 2)
    if n>130: print(n)
