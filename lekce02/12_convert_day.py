week = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
day = input("Enter the number of day, between 1 and 7?")
if not day:
    print("We need number")
elif not day.isnumeric():
    print("Enter the number only")
elif day not in ["1", "2", "3", "4", "5", "6", "7"]:
    print("Only tne numbers between 1 and 7")
else:
    result = int(day) - 1
    print(week[result])



