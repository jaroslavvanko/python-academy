table = [['Name','Age','Email'],
['bob', '23', 'bob@abc.com'],
['ann', '25', 'ann@abc.com'],
['fred', '43', 'fred@abc.com']]
while True:
    print('-'*40)
    print('What do we want to do? Enter the number')
    print('''
1-Create table | 2-Insert new row | 3-Insert new column |
4-Update a cell | 5-Column Total | 6-Row Total | 
7-Print Table | 8-Export do List of Dicts |
''')
    selection = int(input('OPTION: '))
    print('-'*40)
# user want create teble
    if selection == 1:
        table = []
        print("Enter header names seperated by comma.")
        header = input()
        table.append(header.split(","))
# user wants insert new row
    elif selection == 2:
        where = int(input("Row number:"))
        print("Enter the comma separated values:")
        row = input().split(",")
        if 0 < where < len(table):
            table.insert(where,row)
        elif where >= len(table):
            table.append(row)
# user wants to insert a new columm
    elif selection == 3:
        col_name = input("Columm name:")