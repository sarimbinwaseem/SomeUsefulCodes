import math
perp = int(input("Enter perpendicular: "))
base = int(input("Enter Base: "))

hyp = math.sqrt((perp**2)+(base**2))

print("Hypotenuse of triangle is:",round(hyp,3))