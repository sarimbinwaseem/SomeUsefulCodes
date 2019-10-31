txt = input("Enter string to calculate vowels in it: ")

word = list(txt)
x =0
vow = ["a","o","i","e","u"]
for w in word:
	if w in vow:
		print("A vowel found: ",end="")
		print(w)
		x += 1
if x == 0:
	print("No Vowel found...!!!")

print("Total vowels found:", x)
	
