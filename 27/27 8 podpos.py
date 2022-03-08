# maxsum podpos n_ch%30 == 0
f = open("27A (50).txt")
n = int(f.readline())
n_ch = 0
statsumm_by_nch = [10**20]*30
s = 0
maxs = 0
for i in range(n):
    x = int(f.readline())
    s += x
    if x > 0 and x%2 == 0: n_ch += 1
    #Spesial case
    if n_ch%30 == 0: maxs = max(maxs, s)

    maxs = max(maxs, (s - statsumm_by_nch[ n_ch%30 ]))

    statsumm_by_nch[ n_ch%30 ] = min(statsumm_by_nch[ n_ch%30 ], s)
print(maxs)

    
