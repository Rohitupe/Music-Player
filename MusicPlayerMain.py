from tkinter import *
import tkinter as tk
from tkinter import ttk
import tkinter.messagebox as mbox

win  = tk.Tk()
win.title("Music Player")
win.iconbitmap("Icons/icon.ico")
win.resizable(False,False)
win.geometry("500x400")

title = ttk.Label(win,text="All Songs",font="sanserif, 15").pack()

listbox = Listbox(win, height = 10,
                  width = 50,
                  bg = "#a4e0b9",
                  bd=3,
                  activestyle = 'dotbox',
                  font = "Helvetica",
                  fg = "black")
listbox.insert(1,"Hello")
listbox.insert(2,"WOrld")
listbox.pack()

win.mainloop()