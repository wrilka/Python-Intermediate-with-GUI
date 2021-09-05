from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
REPEAT = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_time():
    window.after_cancel(timer)
    timer_label.config(text="Timer")
    checkmark_label.config(text="")
    canvas.itemconfig(text_timer, text="00:00")

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def pull_timer():
    global REPEAT
    REPEAT += 1
    work_sec = WORK_MIN * 60
    mini_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if REPEAT % 2 == 0:
        count_down(mini_break_sec)
        timer_label.config(text="Short Break", fg=PINK)
    elif REPEAT % 8 == 0:
        count_down(long_break_sec)  
        timer_label.config(text="Long Break", fg=RED)    
    else:
        timer_label.config(text="Work", fg=GREEN)
        count_down(work_sec)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(count):
    min = math.floor(count / 60)
    sec = count % 60
    if sec == 0:
        sec = "00"
    elif sec < 10:
        sec = f"0{sec}"
    canvas.itemconfig(text_timer, text=f"{min}:{sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        pull_timer()
        c_mark = ""
        work_ses = math.floor(REPEAT/2)
        for _ in range(work_ses):
            c_mark += "✔"
        checkmark_label.config(text=c_mark)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("My Timer")
window.config(padx=100, pady=50, bg=YELLOW)


timer_label = Label(text="Timer", font=(FONT_NAME, 50, "bold"), fg=GREEN, bg=YELLOW)
timer_label.grid(column=1, row=0)

start_button = Button(text="Start", command=pull_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", command=reset_time)
reset_button.grid(column=2, row=2)

checkmark_label = Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 20))
checkmark_label.grid(column=1, row=3)


canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
my_image = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=my_image)
text_timer = canvas.create_text(100, 130, fill="white", text="00:00", font=(FONT_NAME, 27, "bold"))
canvas.grid(column=1, row=1)


window.mainloop()