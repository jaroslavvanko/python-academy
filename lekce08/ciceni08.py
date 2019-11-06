dataset = [
    ['Name', 'Item', 'Amount', 'Price', 'Total'],
    ['Bettison, Elnora', 'Doxycycline Hyclate', 98, 23.43, 2296.14],
    ['McShee, Glenn', 'DROXIA', 27, 33.86, 914.22],
    ['Conyard, Phil', 'Nadolol', 44, 12.35, 543.4],
    ['Bettison, Elnora', 'Claravis', 91, 9.85, 896.35],
    ['Idalia, Craig', 'Nadolol', 83, 12.35, 1025.05],
    ['Woodison, Annie', 'Metolazone', 46, 43.06, 1980.76],
    ['Woodison, Annie', 'DROXIA', 50, 33.86, 1693.0],
    ['Skupinski, Wilbert', 'Nadolol', 60, 12.35, 741.0],]
# format_header
def format_row(row):
    name, item, amount, unit_price, total_price = row
    return f'|| {name:20} | {item:20} | {amount:>6} | {unit_price:>6.2f} | {total_price:>8.2f} ||'

def format_header(row):
    name, item, amount, unit_price, total_price = row
    return f'|| {name:^20} | {item:^20} | {amount:^5} | {unit_price:^6} | {total_price:^8} ||'

def format_table(table):
    header = format_header(table[0])
    total_width = len(header)
    lines = []
    separator = '=' * total_width
    lines.append(separator)
    lines.append(header)
    lines.append(separator)
    for row in table[1:]:
        lines.append(format_row(row))
    lines.append(separator)
    return '\n'.join(lines)
import pprint
pprint.pprint(dataset)
print(format_table(dataset))