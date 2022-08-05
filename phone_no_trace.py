import phonenumbers
from phonenumbers import timezone, geocoder, carrier
f = open("C:\\Users\\ANKIT\\Desktop\\Python Project\\Trace Phone No\\trace_data.txt","a") # File Handling.

number = input("Enter a no  ")
phone = phonenumbers.parse(number)
# in Variable Phone We are use phonenumbers as a function. Parse will give u the detail of the phone number 
time = timezone.time_zones_for_number(phone) # This Will Give Timezone
car = carrier.name_for_number(phone , "en")
# "en" --> Language is set to english and Car variable will give which company sim does user use
reg = geocoder.description_for_number(phone, "en")
#This will give country of the user.
a = (phone,time,car,reg)
print(phone,time,car,reg)

#File Handling Start
f.write("\n ")
f.write(str(phone))
f.write(str(time))
f.write(str(car))
f.write(str(reg))
f.close()
