f = open('27-52a (1).txt')
n = int(f.readline())
k = [[0]*n for i in range(3)]
for i in range(n):
    x = int(f.readline())
    k[ x%3 ].append( x )
k[0].sort()
k[1].sort()
k[2].sort()

print(max(k[0][-1] + k[1][-1] + k[2][-1],\
          k[0][-1] + k[0][-2] + k[0][-3],\
          k[1][-1] + k[1][-2] + k[1][-3],\
          k[2][-1] + k[2][-2] + k[2][-3]))
    
