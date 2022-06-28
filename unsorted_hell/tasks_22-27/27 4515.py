f = open("27-82b.txt")
n = int(f.readline())
s, os, m = 0, 0, 0
stat = [10**20] * 9
def is_prime(i):
    return all(i%x != 0 for x in range(2, int(i ** 0.5) + 1))

for i in range(n):
    x = int(f.readline())
    s += x
    os += is_prime(x)
    if os % 9 == 0: m = s
    m = max(m, s - stat[os % 9])

    stat[os % 9] = min(stat[os % 9], s)
print(m)
