s = open('24-153.txt').readline()
st, k, m = 0, 1, 10**20
for i in range(len(s) - 1):
    if st == 1 and s[i] == 'F':
        k += 1
        if k > 2: m = min(m, k)
        k, st = 1, 0
    if s[i] == 'A':
        st, k = 1, 1
    if s[i] != 'A' and s[i] != 'F' and st == 1:
        k += 1
print(m)
