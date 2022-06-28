f = open("27-18b.txt")
n = int(f.readline())
a = [int(x) for x in f]
k = 0
for i in range(n):
    end = i + 5
    while end > n: end -= 1
    for j in range(i+1, end):
        if (a[i] + a[j]) % 2 != 0 and (a[i] * a[j]) % 13 == 0:
            k+=1

print(k)

#1 1 1 1 1 1
