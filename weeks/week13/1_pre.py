# -*- coding:utf-8 -*-
from tkinter import *

root = Tk()
root.geometry("640x480")
root.title("Test GUI")

listbox = Listbox(root, selectmode="extended", height=0)
listbox.insert(0, "a")
listbox.insert(1, "b")
listbox.insert(2, "c")
listbox.insert(3, "d")
listbox.insert(END, "e")
listbox.pack()

def btncmd():
    # listbox.delete(0)
    # print(listbox.size())
    # print(listbox.get(0, 2))
    print(listbox.curselection())

btn = Button(root, text="Click", command=btncmd)
btn.pack()

root.mainloop()