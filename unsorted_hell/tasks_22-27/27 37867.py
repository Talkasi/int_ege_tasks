f = open('27-51b.txt')
n = int(f.readline())
s = [[0, 0, 0]]
for i in range(n):
    p = [int(x) for x in f.readline().split()]
    # a[0] - сумма; a[1] - количество четных; a[2] - количество нечетных;
    s = [[a[0]+b,a[1]+(b%2 == 0),a[2] + b%2] for a in s for b in p]
    #print(p)
    #print(s)
    s = {(a[0]%2 , (0 if a[1] > a[2] else 1) if a[1] != a[2] else -1):a for a in sorted(s)[::-1]}
    #print(s)
    #print()
    if i != n - 1: s = s.values()
print(s)
