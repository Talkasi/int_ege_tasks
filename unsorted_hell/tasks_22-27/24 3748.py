s = open('24-157.txt').readline()
ans = []
m = 0

for i in range(len(s) - 2):
    if s[i] == s[i+1]:
        ans.append(s[i+2])

for i in set(ans):
    if m < ans.count(i):
        m = ans.count(i)
        c = i
print(c, m)
    
