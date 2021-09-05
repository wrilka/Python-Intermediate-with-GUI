from os import terminal_size
from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 2
LONG_BREAK_MIN = 20
reps = 0
timer = None

def reset_timer():
    window.after_cancel(timer)
    title_label.config(text="Timer")
    check_label.config(text="")
    canvas.itemconfig(timer_text, text="00:00")

def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    rest_sec = SHORT_BREAK_MIN * 60
    long_sce = LONG_BREAK_MIN * 60

    if reps % 2 == 0:
        title_label.config(text="Rest", fg=PINK)
        count_down(rest_sec)
    elif reps % 8 == 0:
        title_label.config(text="Break", fg=RED)
        count_down(long_sce)
    else:
        title_label.config(text="Work", fg=GREEN)
        count_down(work_sec)


def count_down(count):
    min = math.floor(count/60)
    sec = count % 60
    if sec == 0:
        sec = "00"
    elif sec < 10:
        sec = f"0{sec}"
    canvas.itemconfig(timer_text, text=f"{min}:{sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        check = ""
        check_mark = math.floor(reps/2)
        for _ in range(check_mark):
            check += "✔"
            check_label.config(text=check)



window = Tk()
window.title("Timer App")
window.config(padx=100, pady=50)



my_img = PhotoImage(file="tomato.png")
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
canvas.create_image(100, 112, image=my_img)
timer_text = canvas.create_text(100, 125, text="00:00", fill="white", font=(FONT_NAME, 30, "bold"))
canvas.grid(column=1, row=1)


title_label = Label(text="Timer", font=(FONT_NAME, 40, "bold"), fg=GREEN, bg=YELLOW)
title_label.grid(column=1, row=0)

start_button = Button(text="Start", command=start_timer)
start_button.grid(column=0 , row=2)

reset_button = Button(text="Reset", command=reset_timer)
reset_button.grid(column=2 , row=2)

check_label = Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 30, "bold"), highlightthickness=0)
check_label.grid(column=1 , row=3)

window.mainloop()