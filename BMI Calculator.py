weight = int(input("Enter your weight in KG: "))
height = int(input("Enter your height in cm: "))/100

bmi = weight/(height**2)

print("--------------------")
print("Your BMI is:",bmi)
print("--------------------")

if bmi < 15:
	print("You are very severely underweight!!!!")
elif bmi <= 16:
	print("You are severely underweight!!!!")

elif bmi <= 18.5:
	print("You are underweight")

elif bmi <= 25:
	print("Normal..")
elif bmi <= 30:
	print("You are overweight")

elif bmi <= 35:
	print("Moderately obese")
elif bmi <= 40:
	print("severely obese")
elif bmi > 40:
	print("Very severely obese")











