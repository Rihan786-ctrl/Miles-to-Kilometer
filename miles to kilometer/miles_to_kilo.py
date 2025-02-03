from tkinter import *

def calculate():
    miles = float(miles_input.get())
    km = round(miles * 1.609,4)
    kilometer_result_label.config(text=km)

window = Tk()
window.title("Miles to kilometer Converter ")
window.minsize(width=500, height=500)
window.config(padx=50,pady=50)

miles_input = Entry()
miles_input.grid(column=1,row=0)

miles_label= Label(text="Miles")
miles_label.grid(column=2,row=0)

is_equal_label = Label(text="is equal to ")
is_equal_label.grid(column=0,row=1)

kilometer_result_label=Label(text="0")
kilometer_result_label.grid(column=1,row=1)


kilometer_label = Label(text="Km")
kilometer_label.grid(column=2,row=1)


button = Button(text="Calculate", command=calculate )
button.grid(column=1,row=2)







window.mainloop()
