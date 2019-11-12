names = ['Jacob', 'Jana', 'Petr', 'Klara']
for name in names:
    print(name)
for name in names:
    if name.startswith("J"):
        print(name)
total = 0
for name in names:
    total = total + len(name)
    print(total)