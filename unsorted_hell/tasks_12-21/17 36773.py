a = [int(x) for x in open("17-9.txt")]
ans = []

for i in range(len(a) - 2):
    if ((bin(a[i])[2:]).count('1') >= 3 and (bin(a[i])[2:]).count('0') > 0) +\
       ((bin(a[i + 1])[2:]).count('1') >= 3 and (bin(a[i + 1])[2:]).count('0') > 0) +\
       ((bin(a[i + 2])[2:]).count('1') >= 3 and (bin(a[i + 2])[2:]).count('0') > 0) >= 2:
        ans.append(max(a[i], a[i + 1], a[i+2]))

print(len(ans), max(ans))
