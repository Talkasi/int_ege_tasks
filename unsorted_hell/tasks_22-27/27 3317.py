f = open("27-3A (1).txt")
n, k, d = map(int, f.readline().split())
#a = [int(x) for x in f]
#print(sum(a))
#su = 5002707326 #сумма всех чисел в файле B
su = 5026158 # сумма всех чисел в файле A
s, c, ans = 0, 0, 0
stat = [[0]*d for i in range(k)]

for i in range(n):
    x = int(f.readline())
    s += x

    if s % k == 0 and (su - s) %d == 0: c += 1 #случай с подходящей конкретной суммой
    c += stat[s%k][(su - s) % d]

    #при "отрубании хвостов" лишнее уходит в плюс к оставшейся сумме, поэтому необходимо, чтобы
    #(*остаток суммы в статистике) + (*остаток текущей остающейся суммы) == d
    # * - остаток от деления на D
    stat[s%k][d - (s % d) if s % d !=0 else 0] += 1

print(c)