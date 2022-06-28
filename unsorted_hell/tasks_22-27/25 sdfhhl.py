for x in "1234567890":
    s = int("123567" + x)
    if s % 169 == 0:
        print(s, s//169)

for y in range(1, 10000):
    for x in "1234567890":
        s = int("123" + str(y) + "567" + x)
        if s <= 10**9 and s % 169 == 0:
            print(s, s//169)
        
