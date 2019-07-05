num = int(input("Enter range to calculate sum of +ve integers: "))
sm = 0

for nm in range(num):
	if nm % 2 == 0:
		sm += nm
print("Total sum:",sm)
