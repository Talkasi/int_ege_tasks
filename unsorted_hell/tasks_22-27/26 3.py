f = open("26 (27).txt")
n, s = map(int, f.readline().split())
a = sorted((int(x) for x in f), reverse = 1)
ship = []
last = []
c = 0
i = 0
while sum(a) != (s + 1)*len(a):
    for i in range(len(a)):
        if sum(ship) + a[i] <= s:
            ship.append( a[i] )
            a[i] = s + 1
    last = ship
    ship = []
    c += 1

print(c, sum(last))
        


