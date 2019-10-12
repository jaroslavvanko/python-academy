user_input = input("Give me input:")
if user_input.isalpha():
    print("Letters only")
elif user_input.isnumeric():
    print("Numeric only")
else:
    print("Mixed")