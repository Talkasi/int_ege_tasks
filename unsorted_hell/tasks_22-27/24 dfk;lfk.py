s = open("24 (43).txt").readline().strip()
print(set(s))
s = s.replace("BB", "*").replace("DD", "*")

for i in "ABD":
    s = s.replace(i, ' ')
s = s.split()
print(len(max(s)), max(s))
