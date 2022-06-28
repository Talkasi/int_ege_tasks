for a1 in range(1, 6000//32 + 1):
    for q in range(2, 3000):
        if a1**5 * q ** 10 == 6000:
            print("a) yes,", a1, q)
            break
else:
    print("a) no")
#no

for a1 in range(1, 6000//16 + 1):
    for q in range(2, 3000):
        s = [a1, a1*q, a1*q**2, a1*q**3]
        if (6000 % (a1**4 * q ** 6)) == 0 and \
           ((6000 // (a1**4 * q ** 6)) not in s) and \
           0 < (6000 // (a1**4 * q ** 6)) < 60001:
            print("b) yes,", a1, q, s, (6000 // (a1**4 * q ** 6)))
            break
else:
    print("b) no")
#no

for a1 in range(1, 6000//8 + 1):
    for q in range(2, 3000):
        s = [a1, a1*q, a1*q**2]
        if (6000 % (a1 ** 3 * q ** 3)) == 0 and \
           0 < (6000 // (a1**3 * q ** 3)) < 60001:
            print("c) q =", q, s, '\ta4 * a5 =',(6000 // (a1**3 * q ** 3)))
            break

