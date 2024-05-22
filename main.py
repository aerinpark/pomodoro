from tkinter import *
import math
from tkinter import font

RED = "#FF204E"
GREEN = "#B0C5A4"
BLUE = "#03AED2"
WHITE = "#FFF7F1"
BLACK = "#41444B"
FONT = "Elephant"
CHECK = "✔ "

# in minutes
WORK_TIME = 25
SHORT_BREAK = 5
LONG_BREAK = 15

start = False
timer = None
reps = 0


def reset_timer():
    global timer, start, reps
    window.after_cancel(timer)
    start = False
    reps = 0
    window.config(bg=RED)
    title.config(text="Timer", bg=RED)
    timer_label.config(text="00:00", bg=RED)
    check.config(text="", bg=RED)


def start_timer():
    global start, reps
    reps += 1
    if not start:
        start = True
        # routine: work -> sb -> work -> sb -> work -> sb -> work -> lb and repeat
        if reps % 2 == 1:
            window.config(bg=RED)
            title.config(bg=RED, text="Focus")
            timer_label.config(bg=RED)
            check.config(text=CHECK * math.floor(reps / 2), bg=RED)
            countdown(WORK_TIME * 60)

        elif reps % 8 == 0:
            window.config(bg=GREEN)
            title.config(bg=GREEN, text="Break")
            timer_label.config(bg=GREEN)
            check.config(text=CHECK * math.floor(reps / 2), bg=GREEN)
            reps = 0
            countdown(LONG_BREAK * 60)
        else:
            window.config(bg=BLUE)
            title.config(bg=BLUE, text="Break")
            timer_label.config(bg=BLUE)
            check.config(text=CHECK * math.floor(reps / 2), bg=BLUE)
            countdown(SHORT_BREAK * 60)


def countdown(time_in_sec):
    min = math.floor(time_in_sec / 60)
    sec = time_in_sec % 60

    if sec < 10:
        sec = f"0{sec}"
    timer_label.config(text=f"{min}:{sec}")

    if time_in_sec > 0:
        global timer
        timer = window.after(1000, countdown, time_in_sec - 1)
    else:
        global start
        start = False
        start_timer()


# Create a screen
window = Tk()
window.title("Pomodoro")
window.minsize(width=400, height=300)
window.resizable(width=False, height=False)
window.config(padx=50, pady=50, bg=RED)

# Work Time
title = Label(text="Timer", font=(FONT, 50, "bold"), fg=WHITE, bg=RED, justify="center")
title.grid(column=1, row=0)

# Timer
timer_label = Label(text="00:00", font=(FONT, 30, "bold"), fg=WHITE, bg=RED)
timer_label.grid(column=1, row=1)

# Start button
start_button = Button(text="Start", font=(FONT, 20, "bold"), highlightbackground=WHITE, width=4, fg=BLACK,
                      command=start_timer)
start_button.grid(column=0, row=2, pady=40)

# Reset button
reset_button = Button(text="Reset", font=(FONT, 20, "bold"), highlightbackground=WHITE, width=4, fg=BLACK,
                      command=reset_timer)
reset_button.grid(column=2, row=2, pady=40)

# Check marks
check = Label(text="", font=(FONT, 15, "bold"), bg=RED)
check.grid(column=1, row=2)

window.mainloop()
