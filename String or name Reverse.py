#33
fname = input("enter your first name:")
lname = input("enter your last name:")
str = "" 
str2 = ""
for i in lname: 
	str = i + str
lname = str  
for i in fname: 
   	str2 = i + str2
fname = str2  

name = lname + " " + fname 
  
print ("The reversed string(using loops) is : ",end="") 
print (name)