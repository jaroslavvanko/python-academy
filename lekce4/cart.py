cart = []
repeat = True
while repeat:
    item = input("Enter the price of item or q :")
    if not item.isnumeric():
        continue
    cart.append(float(item))
    answer = input("answer")
    if item == "q" :
        break

        cart.append(float(item))
print("CART" + str(cart))
total_price = 0
i = 0
while i < len(cart):
    total_price = total_price + cart[i]
    i = i + 1
print(total_price)

