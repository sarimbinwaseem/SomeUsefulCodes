#37 NOT RUNNING IN JUPYTER NOTEBOOK
#taking input
print("")

o_number = int(input("Enter the number to be reversed, add to original and be checked for palindrome: "))
#reversing number..
number = int(str(o_number)[::-1])

#adding original and reversed number..
a_number = str(o_number + number)

#checking for Plaindrome
str = "" 
for i in a_number: 
	str = i + str
pal = str
print("")
if a_number == pal:
	print("The answer is palindrome...!!!")
else:
	print("Not a palindrome...")
	