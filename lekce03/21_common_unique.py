# our inputs
string1 = "Bratislava"
string2 = "Praha"
# operation
common = set(string1) & set(string2)
unique = set(string1) - set(string2)
# result
print("Common characters:", common)
print("Unique characters: ", unique)