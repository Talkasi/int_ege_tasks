file = open("27A (48).txt")

number_elem = int(file.readline())

col3 = 0
current_sum = 0
mins = float("inf")

statsum = [-10**20]*number_elem

for i in range(number_elem):
    elem = int(file.readline())

    current_sum += elem

    if elem%3 == 0: col3 += 1

    if col3 == 10:
        mins = min(current_sum, mins)

    mins = min(mins, current_sum - statsum[col3 - 10])

    statsum[ col3 ] = max(col3, current_sum)

print(mins)
