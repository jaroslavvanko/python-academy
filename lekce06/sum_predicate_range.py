def sum_range(start, stop):
    total = 0
    for number in range(start, stop + 1):
        total += number
    return total

def is_prime(number):
    if number <= 0:
        return False
    if number in (1, 2):
        return True
    for i in range(2, (number // 2) + 1):
        if number % i == 0:
            return False
    return True

def sum_prime_range(start, stop):
    total = 0
    for number in range(start, stop + 1):
        if is_prime(number):
            total += number
    return total

def sum_predicate_range(start, stop, predicate):
    total = 0
    for number in range(start, stop + 1):
        if predicate(number):
            total += number
    return total

def is_divisible_by_2(number):
    return number % 2 == 0

print(sum_predicate_range(5, 10, is_prime))
print(sum_predicate_range(5, 10, is_divisible_by_2))

