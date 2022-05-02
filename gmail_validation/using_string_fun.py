email = input("Enter your email: ")  # n@n.np, n@n.com
j = k = l = 0
if len(email)>= 6:
    if email[0].isalpha:
        if ("@" in email) and (email.count("@") == 1):
            if (email[-4] == ".") ^ (email[-3] == "."):
                for i in email:
                    if i == i.upper():
                        j = 1
                    elif i == i.isspace():
                        k = 1

                    elif i == "@" or i == "_" or i == "." or i == i.isdigit:
                        continue
                    else:
                        l = 1
                if j == k == l == 1:
                        print(
                            """Wrong Email- space, uppercase and extra characters except "@ ", "_" and "." are not allowed""")
                else:
                        print("Right Email !")
            else:
                print("""Wrong Email - "." is position is not correct""")

        else:
            print("Wrong Email - Only one @ is compulsory")

    else:
        print("Wrong Email- email must start with alphabet")

else:
    print("Wrong Email- email length must be minimum 6")
