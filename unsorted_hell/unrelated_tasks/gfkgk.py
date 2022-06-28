d = set()
def f(k1, k2, s):
    if s == 5: return k1, k2
    if s < 5:
        d.add(f(k1+3, k2, s+1))
        d.add(f(k1*4, k2, s+1))
        d.add(f(k1, k2+5, s+1))
        d.add(f(k1, k2*2, s+1))

def g(x):
    p = set()
    for i in range(2, int(x**0.5)+1):
        if x%i == 0:
            p.add(i)
            p.add(x//i)
    return [x for x in p]

f(2, 3, 0)
c = 0
x = [j for j in d]
#print(x)
for a in x:
    #print(a)
    h, k = a
    l = k, h
    if l in x: continue
    if all(x%y != 0 for x in g(h) for y in g(k)):
        c += 1
print(c)
