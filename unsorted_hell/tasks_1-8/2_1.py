def task1():
    def f(x, a):
        return (((x % a == 0) and (x % 37 == 0)) <= (x % 3737 == 0)) and (a < 1000)

    for A in range(999, 0, -1):
        if all(f(x, A) for x in range(1, 1000000)):
            print(A)
            break

def task2():
    def f(x, A):
        return (A % 12 == 0) and ((530 % x == 0) <= ((A % x != 0) <= (170 % x !=0)))

    print(len([a
              for a in range(1, 1001)
              if all(f(x, a) for x in range(1, 100_000))]))

def task3():
    def f(x, a):
        return (x & 1097 == 0) <= ((x & 2047 != 0) <= (x & a != 0))
    for A in range(1, 2048):
        if all(f(x, A) for x in range(1, 2048)):
            print(A)
            break

def task4():
    def f(x, a):
        v1 = x % 17 == 0
        v2 = x & 58 == 0
        v3 = x & 8 == 0
        A = x & a == 0
        return ((not v1) <= ((not A) <= (not v2))) <= (v3 and not A and v2)

    for A in range(55, 42, -1):
        if all(f(x, A) == 0 for x in range(1, 64)):
            print(A)
            break

def task5():
    def f(x, y, A):
        return (25*x + 8*y != 10_000) or ((A > x) and (A > y))

    for A in range(100000):
        if all(f(x, y, A) for x in range(2000) for y in range(2000)):
            print(A)
            break

def task6():
    def f(x, y, z, A):
        return (150 != y+2*x+2*z) or (A < x) or (A < y) or (A < z)

    for a in range(10000, 0, -1):
        if all(f(x, y, z, a) == 1
               for x in range(1,151)
               for y in range(1,151)
               for z in range(1,151)):
            print(a)
            break

def task7():
    def f(x):
        P = x in {1, 3, 4, 9, 11, 13, 15, 17, 19, 21}
        Q = x in {3, 6, 9, 12, 15, 18, 21, 24, 27, 30}
        A = False
        return (P <= A) or ((not A) <= (not Q))
    p = 1
    for x in range(1, 50):
        if not f(x):
            p *= x
    print(p)


def task8():
    def f(x, a):
        P = x in {1, 2, 3, 4,5,6,7,8,9,10}
        Q = x in {2, 4, 8, 10}
        A = x in a
        return (Q <= A) and (A <= P)

    a_min = set()
    for X in range(1, 50):
        if not f(X, a_min):
            a_min.add(X)

    a_max = set(range(1, 50))
    for X in range(1, 50):
        if not f(X, a_max):
            a_max.remove(X)

    print(2**len(a_max-a_min))


def task9():
    from itertools import combinations_with_replacement
    def f(x, a, b):
        Q = 175 <= x <= 300
        P = 25 <= x <= 240
        R = 270 <= x <= 340
        A = a <= x <= b
        return (Q <= P) or ((not A) <= R)

    Ox = [i/4 for i in range(341*4)]
    lens = []
    for a1, a2 in combinations_with_replacement(range(341), r=2):
        if all(f(x, a1, a2) for x in Ox):
            lens.append(a2-a1)
    print(min(lens))


def task10():
    from itertools import combinations_with_replacement
    def f(x, a, b):
        Q = 25 <= x <= 42
        P = 1 <= x <= 98
        A = a <= x <= b
        return Q <= (((not P) and (Q)) <= A)

    Ox = [i/4 for i in range(100*4)]
    lens = []
    for a1, a2 in combinations_with_replacement(range(100), r=2):
        if all(f(x, a1, a2) for x in Ox):
            lens.append(a2-a1)
    print(min(lens))