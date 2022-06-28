m = 0
for a in open('24-178.txt'):
    a = a.strip()
    a = a * 2
    k = 1
    for i in range(len(a) - 1):
        if ord(a[i]) <= ord(a[i+1]):
            k += 1
            m=max(m,k)
        else:
            k = 1

print(m)
