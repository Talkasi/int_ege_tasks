f = open('27A (49).txt')
n = int(f.readline())
statsum = [-10**20]*2077
statlen = [0]*2077
min_sum = 10**20
max_minlen = 0
current_sum = 0
for i in range(n):
    elem = int(f.readline())
    current_sum += elem

    #Special case
    if abs(current_sum) % 2077 == 0 and current_sum <= min_sum:
        min_sum = current_sum
        max_minlen = i + 1

    # abs() is a real mistake here
    if (current_sum - statsum[ current_sum % 2077 ]) < min_sum or \
       (current_sum - statsum[ current_sum % 2077 ]) == min_sum and \
        max_minlen < (i + 1 - statlen[ current_sum % 2077 ] ):
        min_sum = current_sum - statsum[ current_sum % 2077 ]
        max_minlen = i + 1 - statlen[ current_sum % 2077 ]

    #Stat
    if statsum[ current_sum % 2077 ] < current_sum:
        statsum[ current_sum % 2077 ] = current_sum
        statlen[ current_sum % 2077 ] = i + 1
print(max_minlen)
        
        

    
