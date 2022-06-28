a = open("24 (44).txt").readline().strip()
#a = "XXYYXZYYZXYZ"
c, m, i = "", "", 0
while i < (len(a) - 1):
    if (a[i] + a[i+2]) == "XY" or (a[i] + a[i+2]) == "ZY":
        c += a[i:i+3]
        m = max(m, c, key = len)
        f = 0
        k = i
        i += 3
    else:
        c = ""
        i -= 2
        if i < k:
            f = 1
        if f:
            i += 3
print(m, len(m)//3)
