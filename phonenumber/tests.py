import phonenumbers
from phonenumbers import geocoder, carrier, timezone
number = str(input("Enter your phone number with +__ : "))
phone = phonenumbers.parse(number) #identify the number (checking whether input is valid or not)
time = timezone.time_zones_for_number(phone) #find timezone of the identified number
service_provider = carrier.name_for_number(phone,"en") # company name , en for english
registered_in = geocoder.description_for_number(phone,"en") # number registered country
print(phone)
print(service_provider)
print(time)
print(registered_in)
