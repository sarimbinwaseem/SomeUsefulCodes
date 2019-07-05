#40
input_string=input("\nType anything:")

letters=0
digits=0
for b in input_string:
	if b.isdigit():
	    digits+=1
	elif b.isalpha():
	    letters+=1

print("There are",letters,"letters and",digits,"digits in the given input...")