item = (43,45,89,789,543,1,678)
def my_min(sequence):
    min = sequence[0]
    for item in sequence[1:]:
        if item < min:
            min = item
    return min
def my_max(sequence):
    max = sequence[0]
    for item in sequence[1:]:
        if item > max:
            max = item
    return max
print(my_max(item))
print(my_min(item))