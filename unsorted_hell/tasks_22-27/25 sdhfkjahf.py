print(126789, 126789//39)
for i in range(1, 1000):
    s = int('12' + str(i) + '6789')
    if s % 39 == 0 and s <= 10**8:
        print(s, s//39)
    
print("\n", 3251*39==126789)
