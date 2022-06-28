s = open('24-173 (1).txt').readline().strip()

l, m = "", ""
for i in range(len(s) - 5):
    if s[i:i+3] != s[i+3:i+6]:
        l += s[i]
    else:
        l += s[i:i+5]
        m = max(m, l, key = len)
        l = ""

if s[-6:-3] != s[-3:]:
    l += s[-5:]
    m = max(m, l, key = len)

print(m, len(m))
        

