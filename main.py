import tkinter

window = tkinter.Tk()
window.title("Miles to KM Convertor")
window.minsize(width=400, height=200)
window.config(padx=50, pady=50)

# Def




# Label - 'is equal to'
equal_label = tkinter.Label(text="is equal to")
equal_label.grid(column=1, row=2)
equal_label.config(padx=10,pady=10)

# Input for Miles
miles_input = tkinter.Entry(width=10)
miles_input.grid(column=2,row=1)
# miles_input.config(padx=10,pady=10) // This generates an error

# Label to display KM value



# Label to say 'KM'



# Button to 'Calculate'



# Stay and Exit
window.mainloop()