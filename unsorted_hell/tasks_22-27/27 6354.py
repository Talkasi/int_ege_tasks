f = open("27-61a.txt")
n = int(f.readline())
s = []
for i in range(n):
    x = int(f.readline())
    s = [x for x in s] + [a+x for a in s] + [x]
    s = {a%100:a for a in sorted(s)}.values()

print(max(x for x in s if x % 100 == 50))

s = '>' +'1'*11 + '2' * 12+ 30*'3'
while '>1' in s or '>2' in s or '>3' in s:
    if '>1' in s:
        s = s.replace('>1', '22>', 1)
    if '>2' in s:
        s = s.replace('>2', '2>', 1)
    if '>3' in s:
        s = s.replace('>3', '1>', 1)

print(sum(int(x) for x in s if x != '>'))
