s = open("24 (42).txt").readline()

s = s.replace("AB", "**").replace("CB", "88")

for i in "ABC":
    s = s.replace(i, ' ')

s = s.split()

print(max([x for x in s], key = len), len(max([x for x in s], key = len)))
