#27B
from math import *
file = open("test.txt")
n = int(file.readline())
arr = [[int(x) for x in f.readline().split()] for i in range(n)]

k = 38
prefix = [0] * (n+1)
#префиксные суммы с 1 до n
for i in range(1, n+1):
    prefix[i] = prefix[i - 1] + int(ceil(arr[i - 1][1] / k))

tmpRes, res = 0, 0
#ищем сумму, если завод в начале массива
for i in range(n):
    tmpRes += abs(arr[i][0] - arr[0][0]) * int(ceil(arr[i][1]/k))

res = tmpRes
pos = 1
for i in range(1, n):
    diff = arr[i][0] - arr[i-1][0]
    tmpRes = tmpRes + diff*prefix[i] - diff * (prefix[n] - prefix[i])
    if res > tmpRes:
        res = tmpRes
        pos = i + 1
print(res, pos)
