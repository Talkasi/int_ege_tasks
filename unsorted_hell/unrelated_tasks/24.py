f = open("24-s1 (1).txt")
m = 10**1000
file = ''
for s in f:
    s = s.strip()
    file += s
    if s.count('A') < m:
        needed_line = s
        m = s.count('A')
chasto = 0
for i in sorted(set(needed_line)):
    print(i, needed_line.count(i), chasto)
    if needed_line.count(i) >= chasto:
        chasto = needed_line.count(i)
        curr = i
slov = {symb:file.count(symb) for symb in sorted(set(file))}
print(curr, slov[(curr)])
print(slov)
        
