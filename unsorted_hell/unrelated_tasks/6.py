a = [int(x) for x in open("17-4 (3).txt")]
ans = []

for i in range(len(a)):
    if len(bin(a[i])[2:]) >3 and (bin(a[i])[2:])[-4:] == '1001':
        print(bin(a[i])[2:])
        s = a[i]
        d = ''
        while s > 0:
            d = str(s % 5) + d
            s = s//5
        if d[-2:] == '11':
            print(d)
            ans.append(a[i])
print(max(ans), sum(ans))
