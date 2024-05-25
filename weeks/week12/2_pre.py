# -*- coding:utf-8 -*-
from tkinter import *

root = Tk()
root.geometry("640x480")
root.title("Test GUI")

entry = Entry(root, width=30, relief="solid")
entry.pack()
entry.insert(0, "Input One Line: ")

label1 = Label(root, text="Entry Input Ouput")
label1.pack()

def change():
    label1.config(text=entry.get())

btn1 = Button(root, text="Click", command=change)
btn1.pack()

text = Text(root, width=30, height=5, relief="solid")
text.pack()
text.insert(1.0, "Input Texts")

label2 = Label(root, text="Text Input Texts Output")
label2.pack()

def change1():
    label2.config(text=text.get(1.0, END))

btn2 = Button(root, text="Click", command=change1)
btn2.pack()

root.mainloop()