import re
email_requirements = "^[a-z]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2,3}$"
email = input('Enter your Email:')

if re.search(email_requirements, email):
    print("Right Email !")
else:
    print("Wrong Email !")