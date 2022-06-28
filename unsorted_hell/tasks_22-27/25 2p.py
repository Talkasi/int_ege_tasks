f = open("26 (17).txt")
n = int(f.readline())
a = sorted(int(x) for x in f)
box1 = []
box2 = []
while a != []:
    box1.append( a.pop(-1) )
    while (sum(box2) <= sum(box1) and a != []):
        box2.append( a.pop(0) )
print(box1)
print(box2)

print(len(box1), len(box2))
