f = open("27B (4).txt")
n = int(f.readline())

c_19 = 0
for i in range(n):
    x = int(f.readline())
    if x%19 == 0: c_19 += 1
print(c_19*(c_19 - 1) * (c_19 - 2)//6)
