numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
i = 0
while i < len(numbers):
    number = numbers[i]
    i = i + 1
    if number % 2 == 1:
        continue
    if number > 10:
        break
    print(number)
