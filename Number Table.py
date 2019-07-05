num = int(input("Enter the number to be tabled:"))

for t in range(1, 11):
	mult = num*t
	print(str(num) + " * " + str(t) + "=" + str(mult))