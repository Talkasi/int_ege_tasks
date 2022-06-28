f = open("27A (30).txt")
n = int(f.readline())
#найти минимальную сумму, кратную 1071*2
m = [100000**30]*(1071*2)
mi = 100000**30
for x in range(n):
    x = int(f.readline())
    ost = 1071*2 - x%(1071*2) if x%(1071*2)!= 0 else 0
    mi = min(mi, x + m[ost])

    m[x%(1071*2)] = min(m[x%(1071*2)], x)
print(mi)

    
