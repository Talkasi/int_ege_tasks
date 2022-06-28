f=open('27A (28).txt')
n=int(f.readline())
q=[int(f.readline()) for i in range(4)]
m=[10**20]*137
mr=-10**20

for i in range(n-4):
    x=int(f.readline())
    ost=x%137
    if m[ost] != 10**20:
        mr=max(mr,abs(x-m[ost]))

    m[q[0]%137]=min(m[q[0]%137],q[0])
    q.append(x)
    q.pop(0)
print(mr)
