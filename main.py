import time
from tkinter import *
from tkinter import messagebox
import threading

timer_speed = 0


def restart():
    text_entry_box.delete("1.0", "end")
    text_entry_box.bind("<Key>", threading.Thread(target=countdown).start())


def add_time(*args):
    global timer_speed
    timer_speed = 10


def countdown(*args):
    global timer_speed
    timer = True
    timer_speed = 10
    while timer:
        time.sleep(1)
        timer_speed -= 1
        text_entry_box.bind("<Key>", add_time)
        # text_entry_box.bind("<Key>", add_time)
        if timer_speed == 0:
            timer = False
    messagebox.showinfo(title="Time Up", message=f"Time UP! The words have cleared because you were idle")
    text_entry_box.delete("1.0", "end")


# ------------------------------------- GUI Configuration -----------------------------------------#


window = Tk()
window.title("Disappearing Text App")
window.minsize(width=1000, height=700)

text_entry_label = Label(window, text="Your text clears if you have stop writing for 10 seconds. Start typing below:")
text_entry_label.grid(row=0, column=1)
text_entry_label.configure(font=("Arial", 20, "bold"))

text_entry_box = Text(height=40, width=150, wrap="word")
text_entry_box.grid(row=1, column=1)
text_entry_box.configure(font=("Arial", 15, "normal"))

text_entry_box.bind("<Key>", threading.Thread(target=countdown).start())

restart_button = Button(window, text="RESTART", command=restart)
restart_button.grid(row=2, column=1)
restart_button.configure(font=("Arial", 20, "bold"))

window.mainloop()
