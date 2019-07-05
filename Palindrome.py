#36
word  = input("Enter word to check for Palindrome: ")

str = "" 
for i in word: 
	str = i + str
pal = str
if word == pal:
	print("This word is palindrome...!!!")
else:
	print("Not a palindrome...")