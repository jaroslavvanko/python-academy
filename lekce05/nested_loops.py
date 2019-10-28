data = [['ID','Name', 'Price', 'Amount', 'Supplier'],
        ['321','Ibalgin', 40.50, 2841, 'Zentiva'],
        ['534','Paralen', 19.90, 3229, 'Zentiva'],
        ['327','Smecta', 68.00, 2709, 'Sipsen'],
        ['242','Uniclophen', 76.00, 476, 'UNIMED']]
# total price
total_price = 0
for row in data[1:]:
    total_price = total_price + row[2] * row[3]
print(total_price)
# total amount
num_items = 0
for row in data[1:]:
    num_items = num_items + row[3]
print(num_items)
# zentiva
zentiva_items = 0
for row in data[1:]:
    if row [4] == "Zentiva":
        zentiva_items = zentiva_items + row[3]
print(zentiva_items)
# dictionary
d = {}
header = data[0][1:]
for row in data[1:]:
    id = row[0]
    d[id] = {}
    for i,item in enumerate(row[1:]):
        key = header[i]
        d[id].update({key: item})
print(d)