email = input("Enter Your Email:") #e@e.np, ab@gmail.com, 
j,k,l=0,0,0
if len(email)>=6:
    if email[0].isalpha():
        if ("@" in email) and (email.count("@")==1):
            if (email[-4]==".") ^ (email[-3]=="."):
                for i in email:
                    if i==i.isspace():
                        k=1
                    elif i.isalpha():
                        if i==i.upper():
                            j=1;
                    elif i.isdigit():
                        continue
                    elif i =="_" or i=="." or i=="@":
                        continue
                    else:
                        l = 1 
                if k == 1 or j == 1 or l == 1:
                    print("Wrong Email - 5 - space and uppercase are not allowed in email")
                else:
                    print("Right Email.")
            else:
                print("""Wrong Email - 4 . position should be either at -4 for .com and -3 for .np""")
        else:
            print("Wrong Email - 3 only one @ is compulsory.")
    else:
        print("Wromg Email - 2 First character should be alphabet")
else :
    print("Wrong Email 1")