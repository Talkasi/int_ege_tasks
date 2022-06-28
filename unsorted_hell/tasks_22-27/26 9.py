f = open("26 (30).txt")
n = int(f.readline())
# 1961 - 30
# 1991 - 0
years = ['']*31
for i in range(n):
    year, typo = map(int, f.readline().split())
    years[1991 - year] += str(typo)
print(years)

c = 0
m = 0
for years_i in range(31):
    years_c = 0
    for mark in range(1, 9):
        if str(mark) not in years[years_i]:
            c += 1
            years_c += 1
    m = max(m, years_c)

for years_i in range(30, -1, -1):
    years_c = 0
    for mark in range(1, 9):
        if str(mark) not in years[years_i]:
            years_c += 1
    if years_c == m:
        needed = years_i
print(c, 1991 - needed)
