#NOTE: Skipped Rewind button, Mute Button

#IMPORTED LIBRARIES
import tkinter as tk
from tkinter import messagebox
from pygame import mixer as mix
from PIL import ImageTk, Image
from tkinter import filedialog
import os  # The guy does this in the tutorial, but there's actually a newer library to do this now.
import pathlib   # This replaced os

#TKINTER STUFF
root = tk.Tk()
root.iconbitmap("Sun.ico")
root.geometry("500x400")
root.title("Cool Music Player")

#PYGAME STUFF
# Initializing the mixer, Before you can do much with pygame, you will need to initialize it.
mix.init()

#FUNCTIONS
def play():
    try:
        mix.music.load(root.filename)
        mix.music.play()
        path_tuple = pathlib.PureWindowsPath(root.filename)  # Syntax to access the individual “parts” (components) of a path using the pathlib library
        status["text"]="Music Playing!" + "\n" + path_tuple.parts[-1] #A tuple giving access to the path’s various components:
        pause_b = tk.Button(root, image=pause_img, command = lambda: pause())
        pause_b.grid(row=0, column=0)
    except:
        mix.music.load(
            "Music Player Project/Mike Perry - The Ocean ft. Shy Martin (Music video).mp3")
        mix.music.play()
        pause_b = tk.Button(root, image=pause_img, command = lambda: pause())    #Pause is declared after play, but the button command still works. Experiemnt with this using normal python, and see if it works differently from tkinter Python.
        pause_b.grid(row=0, column=0)
        status["text"]="Playing Music!" + "\nMike Perry - The Ocean ft. Shy Martin (Music video).mp3"


def pause():
    mix.music.pause()
    play_b = tk.Button(root, image=play_img, command = lambda: unpause())
    play_b.grid(row=0, column=0)
    try:
        path_tuple= pathlib.PureWindowsPath(root.filename)
        status["text"]="Music Paused" + "\n" + path_tuple.parts[-1]
    except:
        status["text"]="Music Paused"


def unpause():
    mix.music.unpause()
    pause_b = tk.Button(root, image=pause_img, command = lambda: pause())
    pause_b.grid(row=0, column=0)
    try:
        path_tuple= pathlib.PureWindowsPath(root.filename)
        status["text"]="Music Playing!" + "\n" + path_tuple.parts[-1]
    except:
        status["text"]="Music Playing!"


def stop():
    mix.music.stop()
    play_b = tk.Button(root, image=play_img, command=lambda: play())
    play_b.grid(row=0, column=0)
    try:
        path_tuple= pathlib.PureWindowsPath(root.filename)
        status["text"]="Music Stopped" + "\n" + path_tuple.parts[-1]
    except:
        status["text"]="Music Stopped" 



#digit=tk.IntVar()  #Since IntVar() is a tkinter specific way to declare a variable, you must put tk before it.
def volume(digit):
    digit = (int(digit)/100)
    mix.music.set_volume(digit)


def about_us():
    messagebox.showinfo("About Us", "Stalk us on Wikipedia ;)")


def open_file():
    root.filename = filedialog.askopenfilename(initialdir="Desktop",
                                               title='Select file', filetypes=(('MP3 files', '*.mp3'), ('M4A files', '*.m4a'), ('FLAC files', '*.flac'), ('WAV files', '*.wav'), ('WMA files', '*.wma'), ('AAC files', '*.aac')))
    # If there is ever an error, maybe decalre filename as global.
    #print(root.filename)

#LABELS
status= tk.Label(root,text="Queue some music to get started!")
status.grid(row=1,column=0, columnspan=4, sticky="w")

#BUTTONS
play_img = ImageTk.PhotoImage(Image.open("play-button.png"))
play_b = tk.Button(root, image=play_img, command=lambda: play())
play_b.grid(row=0, column=0)

pause_img= ImageTk.PhotoImage(Image.open("pause.png"))
# pause_b = tk.Button(root, image=pause_img, command=lambda: pause())
# pause_b.grid(row=0,column=1)

stop_img = ImageTk.PhotoImage(Image.open("stop.png"))
stop_b = tk.Button(root, image=stop_img, command=lambda: stop())
stop_b.grid(row=0, column=2)


#SCALE WIDGET (for volume)
set_vol = tk.Scale(root, from_=0, to=100, orient="horizontal", command=volume)
set_vol.set(50)
set_vol.grid(row=0, column=3)

#MENU WIDGET
# The blank Menu bar
menubar = tk.Menu(root)
root.config(menu=menubar)
#The name of the menu and type of submenu you want in the Menu bar
file_menu = tk.Menu(menubar, tearoff=0)
file_menu.add_command(label="Open", command=open_file)

help_menu = tk.Menu(menubar, tearoff=0)
help_menu.add_command(label="About Cool Music Player", command=about_us)

#The type of menu you want in the Menu Bar
menubar.add_cascade(label="File", menu=file_menu)
menubar.add_cascade(label="Help", menu=help_menu)


#Don't Touch
root.mainloop()
