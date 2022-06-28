s = open("24 (29).txt").readline()
s = s.replace('AB', '-')
s = s.replace('AC', '-')
for i in 'ABC': s = s.replace(i, ' ')
s = s.split()

print(len(max(s, key = len)))

