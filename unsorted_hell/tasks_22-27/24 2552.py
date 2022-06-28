s = open('24-j5.txt').readline()
d = s
while 'SOCKCOSOCKCOS' in s: s = s.replace('SOCKCOSOCKCOS', 'SOCKCOS SOCKCOS')
print(s.count('SOCKCOS'))

c = 0
for i in range(len(d)-6):
    if s[i:i+7] == 'SOCKCOS':
        c +=1
print(c)
