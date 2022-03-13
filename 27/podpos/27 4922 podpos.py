#Task: 4922; sum podpos%k == 0. kolv - ?
#V1 - podpos
f = open("27-97a.txt")
n, k = map(int, f.readline().split())
s, kolv = 0, 0
statk = [0]*k
for i in range(n):
    x = int(f.readline())
    s += x
    #Special case
    if s%k == 0: kolv += 1
    kolv += statk[ s%k ]

    #Stat
    statk[ s%k ] += 1
print(kolv)

