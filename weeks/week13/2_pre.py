# -*- coding:utf-8 -*-
from tkinter import *

root = Tk()
root.geometry("640x480")
root.title("Test GUI")

check_button_variable_1 = IntVar()
check_button_1 = Checkbutton(root, text="Not Today", variable=check_button_variable_1)
# check_button.select()
# check_button.deselect()
check_button_1.pack()

check_button_variable_2 = IntVar()
check_button_2 = Checkbutton(root, text="Weeks", variable=check_button_variable_2)
check_button_2.pack()

def btncmd():
    print(check_button_variable_1.get())
    print(check_button_variable_2.get())

btn = Button(root, text="Click", command=btncmd)
btn.pack()

root.mainloop()