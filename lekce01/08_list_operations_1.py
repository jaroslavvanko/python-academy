employees = ["Anna", "Jacob", "Martin"]
candidates = ["Bruno", "Agnes"]
# delete from candidates
candidates.remove("Bruno")
print(candidates)
# repeat element
candidates = candidates * 3
print(candidates)
# join lists
employees = employees + candidates
print(employees)
# indexing
print(" On index 3 is:", employees[3])
# last index
last_index = len(employees) - 1
print("On index", last_index, "is employee:", employees[last_index])
