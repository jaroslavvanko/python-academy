while True:
    read_file_path = input("Read file")
    try:
        with open(read_file_path) as file:
        content = file.read()
        break
    except FileNotFoundError as exception::
        print(exception)
    else:
        break


write_file_path = input("Write file:")

with open(write_file_path, "w") as file:
    file.write(content)