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

print(sum_prime_range(5, 11))
