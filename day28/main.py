import math
from tkinter import *


PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None


def start_timer():
    global reps
    reps += 1
    if reps % 8 == 0:
        count_down(LONG_BREAK_MIN*60)
        timer_label.config(text="Break!", fg=RED)
    elif reps % 2 == 0:
        count_down(SHORT_BREAK_MIN*60)
        timer_label.config(text="Break!", fg=PINK)
    else:
        count_down(WORK_MIN*60)
        timer_label.config(text="Work!", fg=GREEN)


def reset_timer():
    global timer
    global reps
    reps = 0
    window.after_cancel(timer)
    timer_label.config(text="Timer", fg=GREEN)
    canvas.itemconfig(timer_text, text="00:00")
    check_label.config(text="")


def count_down(count):
    count_min = math.floor(count/60)
    count_sec = count % 60
    canvas.itemconfig(timer_text, text=f"{count_min:02d}:{count_sec:02d}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count-1)
    else:
        start_timer()
        mark = ""
        sessions = math.floor(reps/2)
        for _ in range(sessions):
            mark += "✔"
        check_label.config(text=mark)


window = Tk()
window.title("Pomodoro")
window.config(padx=50, pady=50, bg=YELLOW)


canvas = Canvas(width=300, height=300, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(150, 150, image=tomato_img)
timer_text = canvas.create_text(150, 170, text="00:00", fill="white", font=(FONT_NAME, 22, "bold"))
canvas.grid(column=2, row=2)

timer_label = Label(text="Timer",  font=(FONT_NAME, 30, "bold"))
timer_label.config(fg=GREEN, bg=YELLOW, highlightthickness=0)
timer_label.grid(column=2, row=1)

check_label = Label(font=(FONT_NAME, 20, "bold"))
check_label.config(fg=GREEN, bg=YELLOW, highlightthickness=0)
check_label.grid(column=2, row=4)


start_btn = Button(text="Start", command=start_timer, font=(FONT_NAME, 10, "bold"))
start_btn.grid(column=1, row=3)

reset_btn = Button(text="Reset!", command=reset_timer, font=(FONT_NAME, 10, "bold"))
reset_btn.grid(column=3, row=3)

window.mainloop()
