#Ask the user what hour and mins
hour=int(input("What hour do you see: "))
mins=int(input("What mins do you see: "))

if(hour > 12):
  normal_hour= hour-12
else:
  normal_hour= hour
#print("The normal_hour is: " + str(normal_hour))
print("The normal time is: " + str(normal_hour)+ ":" + str(mins))