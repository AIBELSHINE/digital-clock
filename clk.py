from tkinter import *
from time import strftime

def update_time():
    current_time = strftime("%H:%M:%S %p")
    label.config(text=current_time)
    label.after(1000, update_time)

root = Tk()
root.title("Digital Clock")

label = Label(root, font=("Helvetica", 48), background="black", foreground="white")
label.pack(anchor="center")

update_time()
root.mainloop()
