from tkinter import Tk
from tkinter import Label
import time
import sys

master = Tk()
master.title("Digital Clock")

def get_time():
    timeVar = time.strftime("Jose Urrea %I:%M:%S %p")
    clock.config(text=timeVar)
    clock.after(200, get_time)


clock = Label(master, font=("Calabri", 90), bg="blue", fg="white")
clock.pack()

get_time()

master.mainloop()