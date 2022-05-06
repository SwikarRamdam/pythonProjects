import phonenumbers
from phonenumbers import timezone, geocoder, carrier
number = str(input("Enter your number with +countrycode :  \n"))
phone = phonenumbers.parse(number)
time = timezone.time_zones_for_number(phone)
carier = carrier.name_for_number(phone,"en")
reg = geocoder.description_for_number(phone, "en")
print(phone)
print(carier)
print(time)
print(reg)