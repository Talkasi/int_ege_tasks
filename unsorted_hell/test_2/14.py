s = (16 ** 44) * (16 ** 30) - (8 ** 40 - 8 ** 32) * (16 ** 17 - 32 ** 4) * 32 ** 5
s = hex(s)[2:]
print(s)
s = s.replace('e', '1')
print(s)
s = s[1:]
print(s)
print(s.count('1'))
