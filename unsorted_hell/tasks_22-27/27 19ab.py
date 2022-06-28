f = open('27B (10).txt')
n = int(f.readline())
x_ma = 0
x_mi = 10**100
y_ma = 0
for i in range(n):
    x, y = map(int, f.readline().split())
    if y == 0 and x > x_ma: x_ma = x
    if y == 0 and x < x_mi: x_mi = x
    if y != 0 and abs(y) > y_ma: y_ma = abs(y)

print(abs(x_ma - x_mi)*y_ma // 2)
