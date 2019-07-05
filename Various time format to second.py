#convert all time units in Seconds

millisec = int(input("Enter time duration in MilliSecond: "))
microsec = int(input("Enter time duration in MicroSecond: "))
mint = int(input("Enter time duration in Minute: "))
hour = int(input("Enter time duration in Hour: "))

print("================================================")
print("================================================")
print("From MilliSecond to Second", millisec/1000)
print("From MicroSecond to Second", microsec/100)
print("From Minute to Second", mint*60)
print("From Hour to Second", hour/3600)