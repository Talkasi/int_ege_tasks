f = open("27-20a.txt")
n = int(f.readline())
prev = [int(x) for x in f.readline().split()]
c, m = 1, 1
#2 случая - переставлять нельзя, но с 1 косяк
for i in range(n - 1):
    p = [int(x) for x in f.readline().split()]
    #if p[0] in prev and p[1] in prev and p[1] != p[0]:
        #print("Спорно")
    if p[1] in prev:
        c += 1
        prev = [p[0]]
    elif p[0] in prev:
        c += 1
        prev = [p[1]]
    else:
        m = max(m, c)
        c = 1
        prev = p
m = max(m, c)
print(m)
