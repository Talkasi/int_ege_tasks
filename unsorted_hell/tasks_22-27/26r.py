f = open('26-j9.txt')
s, n = map(int, f.readline().split())
a = [int(f.readline()) for i in range(n)]
a = sorted(a)
ans = []
while sum(ans) < s:
    if sum(ans) + max(a) <= s:
        ans.append(a[-1])
        last = a[-1]
        a.pop( -1 )
    elif sum(ans) + min(a) <= s:
        for i in range(len(a) - 1, -1, -1):
            if sum(ans) + a[i] <= s:
                ans.append(a[i])
                last = a[i]
                a.pop( i )
                break
    if sum(ans) + min(a) <= s:
        ans.append(a[0])
        last = a[0]
        a.pop( 0 )
    else: break
print(a)
print(len(ans), last)
