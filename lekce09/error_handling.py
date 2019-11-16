def count(sequence, target=None):
    if not target:
        return len(sequence)
    else:
        count = 0
        for item in sequence:
            count += item==target
    return count


def my_sum(sequence):
    result = 0
    for i in sequence:
        try:
            result += i
        except TypeError:
            continue
    return result


def avg(sequence):
        return my_sum(sequence) / count(sequence)

print(avg([1,2,3,4,5,"a"]))