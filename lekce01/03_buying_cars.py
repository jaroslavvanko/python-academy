# prices
mercedes = 150
rolls_royce = "400"
extra_equi = int(input("Please enter the extra cost"))
optional_equi = int(input("Please enter the optinal cost"))
# calculation
two_mercedes = mercedes * 2
both_cars = mercedes + int(rolls_royce)
doublerolls_extra = 2 * int(rolls_royce) + 2 * extra_equi
mercedes_optional = mercedes + optional_equi
# result
print("The price for two Mercedes is", two_mercedes, "thousand USD.")
print("The price for Merceddes and Rolls-Royce is", both_cars, "thousand USD.")
print("The price for two Rolls-Royce and extra equipment is", doublerolls_extra, "thousand USD.")
print("The price for Mercedes and optional equipment is", mercedes_optional, "thousand USD.")
