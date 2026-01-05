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
reps = 0
TIMER_TEXT = "WORK"
SHORT_BREAK_TEXT = "5 MIN/nBREAK"
LONG_BREAK_TEXT = "20 MIN/nBREAK"
tick_string = ""
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
    window.after_cancel(timer)
    global reps
    reps = 0
    global tick_string
    tick_string = ""
    global current_state_label
    current_state_label.configure(text="TIMER", fg=GREEN, bg=YELLOW)
    canvas.itemconfig(timer_widget, text="00:00")
    start.config(state="normal")




# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global reps
    start.config(state="disabled")
    reps += 1
    work_secs = WORK_MIN * 60
    short_break_secs = SHORT_BREAK_MIN * 60
    long_break_secs = LONG_BREAK_MIN * 60

    if reps % 2 in [1,3,5,7]:
        current_state_label.configure(text=TIMER_TEXT, fg=GREEN)
        count_down(work_secs)
    elif reps % 8 == 0:
        current_state_label.configure(text=LONG_BREAK_TEXT, fg=RED)
        count_down(long_break_secs)
    elif reps % 8 in [2,4,6]:
        current_state_label.configure(text=SHORT_BREAK_TEXT, fg=PINK)
        count_down(short_break_secs)

"""
Quick thougts on this
we need a way to set the rep to 1 when clicked, and on that click, set first timer
when that timer hits zero, the rep increases and the timer performs the correct timer
Ah, the modulo is for repeateability here. 

The question is how to update the REPS while outside of function. 

"""


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

#so let's say count is 5. Every 1000ms, the count decreases by 1.
#We call the function within the function
def count_down(count):

    count_min = math.floor((count / 60))
    count_sec = count % 60
    if count_sec == 0:
        count_sec = "00"
    elif count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_widget, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1 )
    else:
        start_timer()
        global reps
        global tick_string
        if reps > 0 and reps % 2 == 0:
            tick_string += "✔"
            tick.configure(text=tick_string)



# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)
window.geometry("700x500")
window.resizable(False, False)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)

#here we are specifiying image lcoaiton at X and Y. Halve height and width for this.
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image = tomato_img)

timer_widget = canvas.create_text(100, 130, text="00:00", font=(FONT_NAME, 35, "bold"), fill="white")
canvas.grid(row=1, column=1)


#add widgets to screen

current_state_label = Label(text="TIMER", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50, "bold"))

current_state_label.grid(row=0, column=1)

start = Button(text="Start", bg=YELLOW, highlightbackground = YELLOW, command=start_timer)
start.grid(row=2, column=0)

reset = Button(text="Reset", bg=YELLOW, highlightbackground = YELLOW, command=reset_timer)
reset.grid(row=2, column=2)

#num of ticks needed is reps / 2
tick = Label(text="",fg = GREEN, bg=YELLOW)
tick.grid(row=3, column=1)




#other thing I want is to make the start button inoperable once set.










window.mainloop()