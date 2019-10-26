# Save name
name = input("Enter the name:")
print("Saving", name, "into the name..")
# Save surname
surname = input("Enter the surname:")
print("Saving", surname, "into the surname..")
# Create and print variable full name
full_name = name + " " + surname
print("Full name is:", full_name)
# Create and print variable lenght name
lenght_name = len(full_name)
print("Lenght of full name is:", lenght_name)
# Bounded and print variable full name
print("=" * lenght_name)
print(full_name)
print("=" * lenght_name)