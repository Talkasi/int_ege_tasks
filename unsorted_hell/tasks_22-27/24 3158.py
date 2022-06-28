s = open("24-s2.txt").readline()
#s = 'ABCCAAСZABCADCDD'
st, ma = 0, 0
ans = ''
for i in range(len(s) - 3):
    if s[i] == 'A' and s[i + 2] == 'C': ans += s[i + 1]

for i in set(sorted(ans)):
    if ans.count(i) > ma:
        ma = ans.count(i)
        sy = i
print(sy, ma)
