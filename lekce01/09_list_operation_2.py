# lists candidates and employees
candidates = ['Agnes', 'Agnes', 'Agnes']
employees = ['Francis', 'Bruno', 'Ann', 'Jacob', 'Claire', 'Agnes', 'Agnes', 'Agnes']
# interval 2-5
print("From index 2 to 5 are: ", employees[2:5])
# each 3rd
print("Every third member is: ", employees[::3])
# save index
jacob_index = employees.index("Jacob")
print("Jacob is on index: ", jacob_index)
# find number of Agnes
agnes_count = employees.count("Agnes")
print("Agnes is in list:", agnes_count)