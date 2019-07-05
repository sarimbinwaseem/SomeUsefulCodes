#25
digits = int(input("Enter integer to be sumed up:"))

leng = len(str(digits))
listt = list(str(digits))

sum = 0
for x in range(leng):
	sum += int(listt[x])

print("Total sum of integer is:",sum)