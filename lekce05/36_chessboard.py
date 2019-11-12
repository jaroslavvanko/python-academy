size = 5
sym = ['#',' ']
desk = []

for row in range(size):
    line = []

    for cell in range(size):
        i = (row+cell) % len(sym)
        line.append(sym[i])

    desk.append(''.join(line))

print('\n'.join(desk))