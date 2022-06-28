f = open("27A (61).txt")
n = int(f.readline())
a = []
for i in range(n):
    a += map(int, f.readline().split())
print(a)
