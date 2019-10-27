num = int(input('Please enter your number: '))
result = 0

while num:
    # 1.
    result = result + num**num
    # 2.
    num = num - 1

print(result)