inpt = input("Please write you numbers and press enter:")
nums = inpt.split(",")
result = []
for num in nums:
    num = int(num.strip())
    result.append(num)
print("List:", result)