def f(n):
    return all(n%i != 0 for i in range(2, int(n**0.5)+1))

for s in range(int(106732567**0.25) + 1, int(152673837**0.25)):
    if f(s):
        print(s**4, s**3)
            
