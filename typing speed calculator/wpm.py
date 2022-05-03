from datetime import timedelta
from os import times
from time import *
import random as r
from turtle import textinput

print(time())


def mistake(defaulttext, user_text):
    error = 0
    for i in range(len(defaulttext)):
        try:
            if defaulttext[i] != user_text[i]:
                error = error + 1
        except:
            error = error + 1
    return error


def speed_time(time_s, time_e, user_ip):
    time_delay = time_e - time_s
    time_r = round(time_delay, 2)
    speed = len(user_ip)/time_r
    return round(speed)

if __name__=='__main__':
    while True:
        check = input("Ready ? Yes/ No :\n")
        if check =="yes":
            text = ["This is a string .You have to type for testing your typing speed.",
                        "This program is written in python.", "It uses time and random modules"]
            text1 = r.choice(text)
            print("<--- Typing Speed --->")
            print(text1)
            print()
            print()
            time_1 = time()
            testinput = input("Start Typing :")
            time_2 = time()

            print("Speed : ", speed_time(time_1, time_2, testinput), "w/sec")
            print("Error : ", mistake(text1, testinput))
        elif check == "no":
            print("Thank You ! ")
            break

        else:
            print("Invalid input !")

            

              