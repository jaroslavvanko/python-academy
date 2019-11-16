
    selection = input("Select an option from (1,2,3):"))
    try:
        selection = int(selection)
    except ValueError:
        print("Please inset a number",{selection}, "is not number")
