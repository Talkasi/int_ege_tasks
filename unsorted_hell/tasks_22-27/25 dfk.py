def f(n):
    d = set()
    for i in range(2, int(n ** 0.5)):
        if n%i == 0:
            d.add(i)
            d.add(n//i)
        if len(d) > 2: return []
    return sorted(d)

for i in range(247_264_322, 369_757_523 + 1):
    if int(i ** 0.5) ** 2 == i:
        a = [x for x in sorted(f(i))]
        if len(a) == 2:
            print(i, a[-1])
