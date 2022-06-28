f = open("26 (29).txt")
l, m, n = map(int, f.readline().split())
day = [0] * l
for a in f:
    st, ln = map(int, f.readline().split())
    day[st] = 1
    day[st + ln] = -1

ST, END = 0, -1
for i in range(l):
    
