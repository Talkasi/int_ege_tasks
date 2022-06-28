s = open('24 (26).txt').readline().strip()
c = m = n = s

i = 'XYZ'
while i in s: i += 'XYZ'
while i not in s: i = i[:-1]
print(i, len(i))
ans = len(i)

i = 'YZX'
while i in s: i += 'YZX'
while i not in s: i = i[:-1]
ans += len(i)
print(i, len(i))

i = 'ZXY'
while i in s: i += 'ZXY'
while i not in s: i = i[:-1]
ans += len(i)
print(i, len(i))

print(ans)
