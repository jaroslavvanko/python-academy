# our inputs
string1 = "Bratislava"
string2 = "Budapest"
# operations
difference = set(string1) ^ set(string2)
all = set(string1) | set(string2)
# result
print("Difference characters:", difference)
print("All characters:", all)