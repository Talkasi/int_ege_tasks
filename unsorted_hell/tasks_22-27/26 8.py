f = open("26 (29).txt")
l, m, n = map(int, f.readline().split())
day = [0] * (l+1)
for i in range(n):
    st, ln = map(int, f.readline().split())
    day[st] = 1
    day[st +ln] = -1

k, ST, END = 0, 0, 0
count, ma = 0, 0
for i in range(l+1):
    k0 = k
    k += day[i]
    if k == 0 and ST == 0: ST = i
    if (k == 1 and k0 == 0) or i == l:
        END = i
        if END - ST >= m:
            ma = max(END - ST, ma)
            count += 1
        ST = 0
        END = 0
print(count, ma)
