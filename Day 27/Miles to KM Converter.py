

"""
Steps for completion

TODO 1: import modules and create window of adequte width and height. Add title to window. Add that loop to the end of it

TODO 2: add the elements to the right grid locations:

nothing in 0,0
Entry box for number in 0,1
"Miles" in 0,2
"is equal to" in 1,0
the outputted number in 1,1
"KM" in 1,2
nothing in 2,0
"Calculate" button in 2,1
nothing in 2,2

TODO 3: functionality:

text box should begin with a cursor (focus etc)
calculate button function needs to take the number from the entry, convert, and then display to 1,1
"""

#TODO 1
from tkinter import *

window = Tk()
#give title to the window
window.title("Mile to KM Converter")
#set minimum size for the window
window.minsize(width=300, height= 150)
window.config(padx=20, pady=20)

# TODO 2: add the elements to the right grid locations:

# nothing in 0,0
empty_label = Label(text=" ")
empty_label.grid(row = 0, column = 0)


# Entry box for number in 0,1
entry_box = Entry(width=10)
entry_box.grid(row=0, column=1, padx=40)   # Add horizontal padding
entry_box.focus()



# "Miles" in 0,2

miles_label = Label(text="Miles", font=("Helvetica", 15, "bold"))
miles_label.grid(row=0, column=2)

# "is equal to" in 1,0
equal_to_label = Label(text="Is Equal To", font=("Helvetica", 15, "bold"))
equal_to_label.grid(row=1, column=0)

# the outputted number in 1,1

output_label = Label(text="", font=("Helvetica", 15, "bold"))
output_label.grid(row=1, column=1)

# "KM" in 1,2

km_label = Label(text="KM", font=("Helvetica", 15, "bold"))
km_label.grid(row=1, column=2)

# nothing in 2,0
# "Calculate" button in 2,1

def button_clicked():
    miles_to_convert = int(entry_box.get())
    km_to_output = round((miles_to_convert * 1.60934),2)
    output_label.config(text=km_to_output)

    return

#call the function using the command argument. Note lack of ()
button = Button(text = "Calculate", command = button_clicked)
button.grid(row= 2, column=1)


# nothing in 2,2


# TODO 3: functionality:
#
# text box should begin with a cursor (focus etc)
# calculate button function needs to take the number from the entry, convert, and then display to 1,1
# """


window.mainloop()