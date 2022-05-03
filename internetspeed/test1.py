from tkinter import * 

#from tkinter import * = from tkinter library import everything
#import imports whole library which may not be necessary but from lib import X helps to import specific member(X) of the library
#import module = from lib import *
#tkinter module is used for GUI in python
#library vs modules: library is a collection of modules.Modules are files with .py extension in python, or simply collection of program(functions, codes).

import speedtest
#speed test is a module for testing speed
#pip = preferred installer program is a package installer for python

var = Tk() 
#var is a variable to call tkinter function
var.title("Internet Speed Tester")
var.geometry("300x500")
var.mainloop() 
#var.mainloop provides a window for gui
