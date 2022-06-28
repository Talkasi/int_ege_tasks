f = open("26-66.txt")
n, k = map(int, f.readline().split())
s = 24*1000*60*60
endk = k + s
day = [0]*(s + 1)
for i in range(n):
    st, end = map(int, f.readline().split())
    if (st < endk or st == 0) and (end > k or end ==0):
        if end > endk or end == 0: end = endk
        if st < k or st == 0: st = k
        day[st - k] += 1
        day[end - k] -= 1

print(day[:600])
mx = 0
count = 0
k = 0
for i in range(s+1):
    k += day[i]
    if k > mx: mx, count = k, 0
    if k == mx: count += 1
print(max(day), mx, count)

