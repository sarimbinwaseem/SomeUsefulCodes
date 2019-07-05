#1ft = 30.48 cm

ft = float(input("Enter Enter length in feet: "))

inch = ft*12
yard = ft/3
mile = ft/5280

print("In inches:",inch)
print("In yards:",yard)
print("In miles:",round(mile,3))