import math
x1 = float(input("Enter first X co-ordinate: "))
y1 = float(input("Enter first Y co-ordinate: "))
x2 = float(input("Enter second X co-ordinate: "))
y2 = float(input("Enter second Y co-ordinate: "))

distance = math.sqrt((((x2-x1)**2)+((y2-y1)**2)))

print("Distance between points is:",round(distance, 3))