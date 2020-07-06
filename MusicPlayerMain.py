import pygame

from tkinter import *
import tkinter as tk
from tkinter import ttk
import tkinter.messagebox as mbox

from SearchingSongs import allSong

win  = tk.Tk()
win.title("Music Player")
win.iconbitmap("Icons/icon.ico")
win.resizable(False,False)
win.geometry("500x400")
pygame.mixer.init()

# functions to play and stop
global unpause
unpause = True
def pause():
    global  unpause
    pygame.mixer.music.pause()
    unpause = False

def play():
    global unpause
    if unpause == False:
        pygame.mixer.music.unpause()
        unpause = True
    else:
        songSelect = listbox.get(ACTIVE)
        pygame.mixer.music.load(songSelect)
        pygame.mixer.music.play()

def stop():
    pygame.mixer.music.stop()


title = ttk.Label(win,text="All Songs",font="sanserif, 15").pack()

listbox = Listbox(win, height = 10,
                  width = 50,
                  bg = "#a4e0b9",
                  bd=3,
                  activestyle = 'dotbox',
                  font = "Helvetica",
                  fg = "black",
                  selectmode=SINGLE)
# list all songs
songs = allSong()
count = 1
for song in songs:
    listbox.insert(count,song)
    count+=1
listbox.pack()

# print(listbox.curselection())

# progressbar
pregressBar = ttk.Progressbar(win,orient="horizontal",length=450,mode = 'determinate').pack()


# Buttons play,pause,stop

pauseBtn = ttk.Button(win,text="Pause",command=pause)
pauseBtn.place(x=160,y=280)
playBtn = ttk.Button(win,text="Play",command=play)
playBtn.place(x=80,y=280)
stopBtn = ttk.Button(win,text="Stop",command=stop)
stopBtn.place(x=240,y=280)


win.mainloop()