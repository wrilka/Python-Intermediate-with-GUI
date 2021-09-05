from tkinter import *
import math

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
FONT=(FONT_NAME, 79, "bold")

def start_timer():
    work_time = int(entry_time.get())
    work_min = work_time * 60
    countdown(work_min)

def countdown(time):
    min = math.floor(time/60)
    sec = time % 60
    if sec == 0:
        sec = "00"
    elif sec < 10:
        sec = f"0{sec}"
    
    if time >= 0:
        canvas.itemconfig(my_text, text=f"{min}:{sec}")
        windows.after(1000, countdown, time-1)






windows = Tk()
windows.title("MY TIMER APP")
windows.config(padx=40, pady=20)


canvas = Canvas(width=500 , height=490)
photo = PhotoImage(file="apple.png")
canvas.create_image(250, 490/2, image=photo)
my_text = canvas.create_text(250, 279, text="00:00", fill="white", font=FONT)
canvas.grid(column=0, row=1, columnspan=2)


button_start = Button(text="START", bg=GREEN, font=("Ariel", 15, "normal"), command=start_timer)
button_start.grid(column=0, row=2)

button_reset = Button(text="RESET", bg=RED, font=("Ariel", 15, "normal"))
button_reset.grid(column=1, row=2)

time_label = Label(text="Enter time here in MIN            ", font=(FONT_NAME, 17, "normal"))
time_label.grid(column=0, row=0, columnspan=2)

entry_time = Entry(bg=GREEN, width=15)
entry_time.focus()
entry_time.grid(column=1, row=0)

windows.mainloop()