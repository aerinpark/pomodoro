from tkinter import *

RED = "#FF204E"
GREEN = "#B0C5A4"
BLUE = "#03AED2"
WHITE = "#FFF7F1"
BLACK = "#41444B"
FONT = "Elephant"

# Create a screen
window = Tk()
window.title("Pomodoro")
window.minsize(width=300, height=300)
window.config(padx=20, pady=50, bg=RED)

# Work Time
title = Label(text="Timer", font=(FONT, 50, "bold"), fg=WHITE, bg=RED)
title.grid(column=1, row=0)

# Timer
timer_label = Label(text="00:00", font=(FONT, 30, "bold"), fg=WHITE, bg=RED)
timer_label.grid(column=1, row=1)

# Start button
start_button = Button(text="Start", font=(FONT, 20, "bold"), highlightbackground=RED, width=4, fg=BLACK)
start_button.grid(column=0, row=2, pady=40)

# Reset button
reset_button = Button(text="Reset", font=(FONT, 20, "bold"), highlightbackground=RED, width=4, fg=BLACK)
reset_button.grid(column=2, row=2, pady=40)

window.mainloop()