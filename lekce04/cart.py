cart = []
repeat = True
while repeat:
    item = float(input("Enter the price:"))
    cart.append(item)

    answer = input("Press enter or q for quit program")
    if answer == "q":
        repeat = False
i = 0
repeat = True
while repeat:
    index = i % len(cart)
    print(cart[index])
    answer = input("Press enter or q for quit")
    if answer == "q":
        repeat = False
    else:
        i = i + 1
i = 0
total_price = 0
while i < len(cart):
    total_price = total_price + cart[i]
    i = i + 1

print("Cart:" + str(cart))
print("Total price:" + str(total_price))


