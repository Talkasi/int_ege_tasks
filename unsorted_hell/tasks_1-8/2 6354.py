k = 0, 1

for x in k:
    for y in k:
        for z in k:
            if not(((not (x)) or y or z) and ((not (x)) or (not(z)))):
                print(x, y, z)

a = [int(x) for x in open("17-3.txt")]
ans = []
for i in range(len(a) - 2):
    if (a[i] % 3 == 0) and (a[i+1] % 3 == 0) and (a[i+2] % 3 == 0) and \
       ((a[i]%12 == 0) or (a[i+1]%12 == 0) or (a[i+2]%12 == 0)):
        ans.append((a[i] + a[i+1] + a[i+2])//3)
print(len(ans), min(ans))
