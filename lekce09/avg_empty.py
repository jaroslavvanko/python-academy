def avg(sequence):
    try:
        return sum(sequence) / len(sequence)
    except ZeroDivisionError:
        return 0.0
#print(avg([]))
print(avg([]))

