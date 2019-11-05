def identity(item):
    return item

def maximum(*args, default = None, key = identity):
    if not args:
        return default
    max_value = key(args[0])
    max_item = args[0]
    for item in args[1:]:
        key_item = key(item)
        if key_item > max_value:
            max_value = key_item
            max_item = item
    return max_item

print(maximum("Aš", "Brno", "Pardubice", "Praha"))
print(maximum("Aš", "Brno", "Pardubice", "Praha", key=len))




