# Task: find max_sum with min_len, max_sum%69 == 0
file = open("27_B (1).txt")
num_el = int(file.readline())

current_sum = 0
stat_sum = [-10**20]*69  ## This one should be 10**20 - it makes the solution simpler
stat_len = [0]*69
max_sum = -10**20
min_maxsumlen = 0

#Addition:
#           Comments were used to find the mistake
#           ## - addings after solution has been seen


for i in range(num_el):
    elem = int(file.readline())
    current_sum += elem

    # Special case
    if current_sum % 69 == 0:
        #print('Special case')
        #print('max_sum: ', max_sum)
        #print('min_maxsumlen: ', min_maxsumlen)
        max_sum = current_sum
        min_maxsumlen = i + 1
        #print('max_sum after: ', max_sum)
        #print('min_maxsumlen after: ', min_maxsumlen, '\n')

    # When our sum is bigger and `sum%69 == 0`
    if (current_sum - stat_sum[ current_sum % 69 ]) > max_sum and stat_sum[ current_sum % 69 ] != -10**20:
        #print('Our sum is bigger and `sum%69 == 0`')
        #print('max_sum: ', max_sum)
        #print('min_maxsumlen: ', min_maxsumlen)
        max_sum = current_sum - stat_sum[ current_sum % 69 ]
        min_maxsumlen = i + 1 - stat_len[ current_sum % 69 ]
        #print('max_sum after: ', max_sum)
        #print('min_maxsumlen after: ', min_maxsumlen, '\n')

    ## This two cases can be written as one

    # When our sum is equal but len is lower
    if max_sum == (current_sum - stat_sum[ current_sum % 69 ]) and \
       min_maxsumlen > (i + 1 - stat_len[ current_sum % 69 ]):
        #print('Our sum is equal but len is lower')
        #print('min_maxsumlen: ', min_maxsumlen)
        min_maxsumlen = i + 1 - stat_len[ current_sum % 69 ]
        #print('min_maxsumlen after: ', min_maxsumlen, '\n')

    if stat_sum[ current_sum % 69 ] > current_sum or stat_sum[ current_sum % 69 ] == -10**20:
        #print('Stat changing')
        #print('stat_sum: ', stat_sum)
        #print('stat_len: ', stat_len)
        stat_sum[ current_sum % 69 ] = current_sum
        stat_len[ current_sum % 69 ] = i + 1
        #print('stat_sum after: ', stat_sum)
        #print('stat_len after: ', stat_len, '\n')
print(min_maxsumlen)
    
    
