f = open('24-s1.txt')
all_file = ""
max_n_symb = 0
#check all lines
for s in f:
    all_file += s
    n_pairs = 0
    #count pairs
    for i in range(len(s) - 1):
        if ord(s[i])+1 == ord(s[i+1]):
            n_pairs += 1
    #check if it is more pairs then we had
    if n_pairs >= max_n_symb:
        needed_line = s
        max_n_symb = n_pairs
        
min_n_symb = 10**20
#find less used symb
for i in set(needed_line.strip()):
    if min_n_symb > needed_line.count(i):
        min_n_symb = needed_line.count(i)
        find_symb = i

print(find_symb, all_file.count(find_symb))
