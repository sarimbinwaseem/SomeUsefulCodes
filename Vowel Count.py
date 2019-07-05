txt = input("Enter string to calculate vowels in it: ")

word = list(txt)
x =0
for w in word:
	if w == 'a' or w == 'e' or w == 'i' or w == 'o' or w == 'u':
		print("A vowel found: ",end="")
		print(w)
		x += 1
if x == 0:
	print("No Vowel found...!!!")

print("Total vowels found:", x)
	