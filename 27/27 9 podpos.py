f = open('27_B (3).txt')
# len >= 5, sumel%117 == 0, n - ?
n = int(f.readline())
s = 0
q = []
for i in range(4):
    x = int(f.readline())
    s += x
    q.append(s)
st = [0]*117
k = 0
for i in range(n - 4):
    x = int(f.readline())
    s += x
    #Spesial case
    if s%117 == 0: k += 1
    k += st[ s%117 ]

    st[ q[0]%117 ] += 1
    q.pop(0)
    q.append(s)
print(k)
