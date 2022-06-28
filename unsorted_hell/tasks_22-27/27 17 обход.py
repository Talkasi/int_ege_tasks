f = open("27A (30).txt")
n = int(f.readline())
#найти минимальную сумму, кратную 1071*2
a = [int(x) for x in f]
m = [100000**30]*(1071*2)
mi = 100000**30
for i in range(n):
    for j in range(i+1, n):
        if j - i <= 11:
            if (a[i] + a[j])%(1071*2) == 0:
                mi = min(mi, (a[i] + a[j]))
print(mi)

    
