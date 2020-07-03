from tkinter import *
import tkinter as tk
from tkinter import ttk
import pygame

"""pip install pygame"""

win = tk.Tk()
win.title("Play Sound With Click")
win.geometry("400x300")
# win.iconbitmap("image .ico path")
pygame.mixer.init()
def play():
    pygame.mixer.music.load(r"C:\Users\Rohit\Downloads\Shiva.mp3")
    pygame.mixer.music.play(loops=0)

def pause():
    pygame.mixer.music.pause()

def unpause():
    pygame.mixer.music.unpause()

def stop():
    pygame.mixer.music.stop()

playBtn = ttk.Button(win,text="Play Sound",command=play).pack(pady=30)

unpauseBTN = ttk.Button(win,text="Unpause Sound",command=unpause).pack(pady=30)

pauseBtn = ttk.Button(win,text="Pause Sound",command=pause).pack(pady=30)

stopBtn = ttk.Button(win,text="Stop Sound",command=stop).pack(pady=30)

win.mainloop()