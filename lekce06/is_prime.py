def is_prime(number):
    if number <= 0:
        return False
    if number in (1, 2):
        return True
    for i in range(2, (number // 2) + 1):
        if number % i == 0:
            return False
    return True
for i in range(1, 13):
    print(i, is_prime(i))
