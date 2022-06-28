f = open("26-52.txt")
n = int(f.readline())
a = sorted(int(x) for x in f)
c = 0
for i in range(n):
    for j in range(i+1, i + 102):
        if j < n:
            if (a[i]+a[j]) % 10 == 0:
                c+=1
print(c)
    
