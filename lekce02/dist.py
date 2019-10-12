import math
point_ax = float(input("Point A, Coordinate X:"))
if point_ax < 0:
    print("No way broo")
point_ay = float(input("Point A, Coordinate Y:"))
point_bx = float(input("Point B, Coordinate X:"))
point_by = float(input("Point B, Coordinate Y:"))

a = abs(point_ax - point_bx)
b = abs(point_ay - point_by)

dist = round(math.sqrt( a ** 2 - b ** 2), 2)
print(dist)