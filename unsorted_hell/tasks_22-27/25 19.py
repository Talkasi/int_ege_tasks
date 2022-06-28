def f(n):
    return all(n%i != 0 for i in range(2, int(n**0.5) + 1))

for i in range(113_000_000, 114_000_001, 2):
    if i // 2 % 2 != 0 and int((i//2)**0.5) ** 2 == i//2 and f(int((i//2)**0.5)):
        print(i, int((i//2)** 0.5) * 2)
