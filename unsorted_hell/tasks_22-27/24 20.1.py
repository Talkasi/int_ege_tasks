max_symb_n_line = 0
max_symb_n_file = 0
all_lines = ''

for line in open('24 (28).txt'):
    line = line.strip()
    all_lines = all_lines + line

    # Check each symbol from line
    for current_simb in set(line):
        line_update = line

        for other_simb in set(line):
            if other_simb != current_simb:
                line_update = line_update.replace(other_simb, ' ')

        # Create list from line_update
        line_update = line_update.split()

        # Find max symb*n line
        if len(max(line_update)) > max_symb_n_file:
            max_symb_n_file = len(max(line_update))
            needed_line = line

max_symb_met = 0

for symb in sorted(set(needed_line)):
    print(symb, needed_line.count(symb))
    if needed_line.count(symb) > max_symb_met:
        max_symb_met = needed_line.count(symb)
        needed_symb = symb

print(needed_symb, all_lines.count(needed_symb))

