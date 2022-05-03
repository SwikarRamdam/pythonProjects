from cProfile import label
from cgitb import text
import imp
from tkinter import *
from click import command
import speedtest

def speedCheck():
    vs = speedtest.Speedtest()
    #vs is a variable for speedtest like vt for tkinter
    #calling Speedtest class inside speedtest module
    vs.get_servers()
    down = str(round(vs.download()/(10**6),3)) + " Mbps"
    #checks download speed bits/sec , dividing by 10^6 gives Mega bits persecond(Mbps)
    up = str(round(vs.upload()/(10**6),3))+ " Mbps"
    labd.config(text = down)
    labu.config(text = up)

vt = Tk()

vt.title("Internet Speed Tester")
vt.geometry("500x500")
vt.config(bg="")
#config is used to configure the window

#LABEL

lab = Label(vt, text = "Internet Speed Tester",font = ("Times New Roman",25, "bold"),fg="black") 
#vt function should be called everytime
lab.place(x=55,y = 40,height=50, width=380)


lab = Label(vt, text = "Downloading Speed ",font = ("Times New Roman",25,"bold"), fg="black")
lab.place(x = 55, y = 130, height=50, width=380)   #y = y+ht+gap(40)


labd = Label(vt, text = "00",font = ("Times New Roman",25,"bold"), fg="black")
labd.place(x = 55, y = 200, height=50, width=380)


lab = Label(vt, text = "Uploading Speed ",font = ("Times New Roman",25,"bold"), fg="black")
lab.place(x = 55, y = 290, height=50, width=380)


labu = Label(vt, text = "00",font = ("Times New Roman",25,"bold"), fg="black")
labu.place(x = 55, y = 360, height=50, width=380)

#BUTTONS

btn = Button(vt, text="Check",font = ("Times New Roman",25,"bold"),relief = RAISED,bg="#4287f5",command=speedCheck)
btn.place(x = 55,y = 435,height=50, width=380)

vt.mainloop()