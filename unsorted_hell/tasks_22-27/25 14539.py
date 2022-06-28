def f(n):
    d = set()
    for i in range(1, int(n**0.5) + 1):
        if n%i == 0:
            if i%2 == 0: d.add(i)
            if n//i % 2 == 0: d.add(n//i)
    return sorted(d)

def m(n):
    d = set()
    for i in range(1, int(n**0.5) + 1):
        if n%i == 0:
            d.add(i)
            d.add(n//i)
    return sorted(d)

for i in range(190201, 190261):
    a = [x for x in f(i)]
    a1 = [x for x in m(i) if x % 2 == 0]
    if a != a1: print("error")
    if len(a) == 4:
        print(a[-1], a[-2])
