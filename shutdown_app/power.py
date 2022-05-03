from tkinter import *
import os

def restart():
    os.system("shutdown /r /t 1") # after 1 seconds
def schedule_restart():
    os.system("shutdown /r /t 20") # after 20 seconds
def logout():
    os.system("shutdown -l")
def shutdown():
    os.system("shutdown /s /t 1")


st = Tk()
st.title("shutdown app")
st.geometry("500x500")
st.config(bg = "green")


restart_button = Button(st , text="Restart",font=("Times New Roman",20,"bold"),relief=RAISED,cursor = "plus",command=restart())
restart_button.place(x=180,y=100,height=50,width=150)

restart_w_time_button = Button(st , text="Schedule Restart",font=("Times New Roman",20,"bold"),relief=RAISED,cursor = "plus",command=schedule_restart())
restart_w_time_button.place(x=155,y=200,height=50,width=200)

log_out_button = Button(st , text="Log out",font=("Times New Roman",20,"bold"),relief=RAISED,cursor = "plus",command = logout())
log_out_button.place(x=180,y=300,height=50,width=150)

shutdown_button = Button(st , text="Shut Down",font=("Times New Roman",20,"bold"),relief=RAISED,cursor = "plus",command = shutdown())
shutdown_button.place(x=180,y=400,height=50,width=150)

st.mainloop()