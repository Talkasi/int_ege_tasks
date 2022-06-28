f = open("26-39 (2).txt")
n, m = map(int, f.readline().split())
big, small = [], []
for i in range(n):
    x = int(f.readline())
    if 180 <= x <= 200: big.append(x)
    else: small.append(x)
big = sorted(big)[::-1]
small = sorted(small)
ship = []

while sum(ship) < m:
    if len(big) > 0 and sum(ship) + big[0] < m:
        ship.append(big[0])
        big.pop(0)
    elif len(small) > 0 and sum(ship) + small[0] < m and m - sum(ship) - small[0] > small[1]:
        ship.append(small[0])
        small.pop(0)
    else:
        for i in range(len(small)):
            if sum(ship) + small[i] > m:
                ship.append(small[i-1])
                break
        break
print(len(ship), sum(ship))
