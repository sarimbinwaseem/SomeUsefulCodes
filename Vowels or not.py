char = input("Enter number: ")

vowels = ['a','e','i','o','u']
leng = len(vowels)
for x in range(leng):
	if char ==vowels[x]:
		print("This letter is vowel...")
		break
	else:
		print("Not a vowel....")
		break

