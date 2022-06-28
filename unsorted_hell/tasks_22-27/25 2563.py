def f(n):
    return all(n%i!= 0 for i in range(2, int(n**0.5)+1))
c = 0
for n in range(3532000, 3532161):
    if f(n):
        c += 1
        print(c, n)
