num = input("Give me a number:")
if num == "":
    print("Number??")
else:
    mid_point = len(num) // 2
first_half = int(num[:mid_point])
second_half = int(num[mid_point:])

if first_half % 2 == 0 and second_half % 2 == 0:
    print("Success")
elif first_half % 2 == 0:
    print("first")
elif second_half % 2 == 0:
    print("Seconf")
else:
    print("Neither")