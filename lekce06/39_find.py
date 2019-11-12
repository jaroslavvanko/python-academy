seq = (['pear', 'apple', (23, 45), 653, {'name': 'John'}] , {'name': 'John'})
def my_find(seq, item):
    for i, obj in enumerate(seq):
        if obj == item:
            return i
    return -1
print(my_find(item(i)