a = open('24-2.txt').readline()
c = a[0]
m = ''
for i in range(len(a) - 1):
    if a[i] > a[i+1]:
        c += a[i+1]
    else:
        m = max(m, c, key = len)
        c = a[i+1]
print(m, len(m))
