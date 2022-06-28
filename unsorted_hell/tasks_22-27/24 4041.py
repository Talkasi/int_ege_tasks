m = 0
for s in open('24-164.txt'):
    if s.count('G') < 15:
        for i in set(s):
            m = max(m, s.rfind(i) - s.find(i))
print(m)
