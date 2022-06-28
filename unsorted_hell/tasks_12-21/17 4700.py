f = open("17-243.txt")
a = [int(x) for x in f]
ma = max(x for x in a if x%173 == 0)
ans = []
for i in range(len(a) - 1):
    if a[i] > ma or ma < a[i+1]:
        ai, ai2 = a[i], a[i+1]
        ani, ani2 = "", ""
        while ai > 0:
            ani += str(ai%3)
            ai = ai//3
        while ai2 > 0:
            ani2 += str(ai2%3)
            ai2 = ai2//3 
        if '22' in ani or '22' in ani2:
            ans.append(a[i]+a[i+1])
print(len(ans), min(ans))

