a = [int(x) for x in open("17.txt")]
ans = []

for i in range(len(a) - 1):
    if abs(a[i] + a[i+1])%2 == 0 and abs(a[i] + a[i+1])%10 != 6:
        ans.append((a[i] + a[i+1])//2)

print(len(ans), max(ans))
