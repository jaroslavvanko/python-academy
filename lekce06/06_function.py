def sum_range(start, stop):
    total = 0
    for number in range(start, stop + 1):
        total += number
    return total
print(sum_range(5, 10))