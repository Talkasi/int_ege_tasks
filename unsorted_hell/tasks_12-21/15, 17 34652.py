for a in range(1, 10000000):
    if all(x//50>3 or x//13<=3 or x//a > 6 for x in range(1, 10000)):
        print(a)
        break

def f(n):
    if n <= 2 or n == 8: return 0
    if n == 3: return 1
    if n > 3 and n!= 8: return f(n - 2) + f(n - 1)

for i in range(0, 100000):
    if f(i) == 25:
        print(i)
        break
print(f(13), '\n')


a = [int(x) for x in open('17-199 (1).txt')]
ans = []

for i in range(len(a) - 2):
    if (not(a[i] > 0 and 100<=a[i]<1000 and a[i]%2 != 0)) and \
       (a[i + 1] > 0 and 100<=a[i + 1]<1000 and a[i + 1]%2 != 0) and \
       (not(a[i + 2] > 0 and 100<=a[i + 2]<1000 and a[i + 2]%2 != 0)):
        ans.append(a[i] + a[i+1] + a[i+2])
print(len(ans), max(ans))



    
