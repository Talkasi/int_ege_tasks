s = open('24 (16).txt').readline()
c =  'DBAC' 
while c in s: c += 'DBAC'
while not c in s: c = c[:-1]
print(c, len(c))
