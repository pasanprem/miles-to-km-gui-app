import tkinter

window = tkinter.Tk()
window.title("Miles to KM Convertor")
window.minsize(width=400, height=200)
window.config(padx=50, pady=50)

# Functions
def button_clicked():
    mile_value = float(miles_input.get())
    km_value = mile_value * 1.6
    kmresult_label.config(text=km_value)

# Label - 'is equal to'
equal_label = tkinter.Label(text="is equal to")
equal_label.grid(column=1, row=2)
equal_label.config(padx=10,pady=10)

# Input for Miles
miles_input = tkinter.Entry(width=10)
miles_input.grid(column=2,row=1)
# miles_input.config(padx=10,pady=10) // This generates an error

# Label to say 'Miles'
Miles_label = tkinter.Label(text="Miles")
Miles_label.grid(column=3,row=1)

# Label to display KM value
kmresult_label = tkinter.Label(text="0.00")
kmresult_label.grid(column=2,row=2)

# Label to say 'KM'
KM_label = tkinter.Label(text="KM")
KM_label.grid(column=3,row=2)

# Button to 'Calculate'
calc_button = tkinter.Button(text="Calculate", command=button_clicked)
calc_button.grid(column=2,row=3)

# Stay and Exit
window.mainloop()