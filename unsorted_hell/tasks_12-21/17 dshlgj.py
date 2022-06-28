a = [int(x) for x in open("17 (14).txt")]
sr =  sum(a) / len(a)
print(sr)
ans = []
for i in range(len(a) - 1):
    if a[i] < sr and a[i+1] < sr and (a[i]%10 == 9 or a[i+1] % 10 == 9):
        ans.append(a[i] + a[i+1])
print(len(ans), max(ans))

a=[int(x) for x in open('17 (14).txt')]
sr=5442.9905
ans=[]
for i in range(len(a)-1):
    if (a[i]<sr) and (a[i+1]<sr) and ((a[i]%10==9) or (a[i+1]%10==9)):
        ans.append(a[i]+a[i+1])
print(len(ans),max(ans))
