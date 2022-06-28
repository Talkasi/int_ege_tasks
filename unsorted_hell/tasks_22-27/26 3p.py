f = open("26 (18).txt")
c, summ = 0,0
n, s = map(int, f.readline().split())
a = sorted(int(x) for x in f)

ship = []
while a != []:
    while sum(ship) + a[-1] <= s:
        ship.append( a.pop(-1) )
        if a == []: break
    print(c, summ, ship)
    c += 1
    summ += sum(ship)
    ship  = []
print(c, summ)
