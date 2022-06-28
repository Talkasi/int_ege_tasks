f = open("27A (2).txt")
n = int(f.readline())
a = [int(x) for x in f]
c = 0
for i in range(n):
    for j in range(i+1, n):
        if a[i]*a[j] %65 == 0:
            c+=1
print(c)

