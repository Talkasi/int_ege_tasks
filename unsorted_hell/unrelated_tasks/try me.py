f = open("C:/Users/Talkasi/Desktop/КПоляков/27data/7/27.txt")
n = int(f.readline())

k1, k2 = 0, 0
for i in range(n):
    x = int(f.readline())

    if x%7 == 0 and x%49 != 0: k1 = max(k1, x)
    if x%7 != 0: k2 = max(k2, x)
print(k1 * k2)
