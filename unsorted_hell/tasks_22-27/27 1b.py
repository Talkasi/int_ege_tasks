f = open("27B.txt")
n = int(f.readline())

c = c1 = 0
for i in range(n):
    x = int(f.readline())
    if x%2 == 0: c += 1
    else: c1 += 1

print(c*(c - 1)//2 + c1*(c1 - 1)//2)
