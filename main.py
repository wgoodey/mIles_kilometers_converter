from tkinter import *

TO_KM = 1.609344
TO_MILES = 0.621371
MILES = "Miles"
KILOMETERS = "Kilometers"
factor = TO_KM

window = Tk()
window.title("Miles/Kilometers Converter")
window.config(padx=25, pady=25)

textbox = Entry(width=10)
textbox.insert(END, string="0")
textbox.grid(column=0, row=0)

base_unit = Label(text="Miles", padx=15, pady=15)
base_unit.grid(column=1, row=0)

converted_unit = Label(text="Kilometers", padx=15)
converted_unit.grid(column=1, row=1)

result = Label(text=0)
result.grid(column=0, row=1)


def reverse_conversion():
    global factor

    if base_unit["text"] == MILES:
        base_unit.config(text=KILOMETERS)
        converted_unit.config(text=MILES)
        factor = TO_MILES
    else:
        base_unit.config(text=MILES)
        converted_unit.config(text=KILOMETERS)
        factor = TO_KM

    convert()


def convert():
    value = float(textbox.get()) * factor
    result.config(text="{:.5f}".format(value))


reverse_button = Button(text="Reverse", command=reverse_conversion)
reverse_button.grid(column=2, row=1)

calculate_button = Button(text="Calculate", command=convert)
calculate_button.config(padx=15, pady=5)
calculate_button.grid(column=3, row=2)

window.mainloop()
