import tkinter

FONT = ("Arial", 10)


def calculate():
    miles = int(miles_input.get())
    km = miles*1.609
    calc_label["text"] = str(km)


window = tkinter.Tk()
window.title("Miles to KM converter")
window.minsize(width=300, height=100)
window.config(padx=50, pady=50)

miles_input = tkinter.Entry()
miles_input.grid(column=1, row=0)

miles_label = tkinter.Label(text="Miles", font=FONT)
miles_label.grid(column=2, row=0)

text_label = tkinter.Label(text="is equal to", font=FONT)
text_label.grid(column=0, row=1)

calc_label = tkinter.Label(text="0", font=FONT)
calc_label.grid(column=1, row=1)

km_label = tkinter.Label(text="km", font=FONT)
km_label.grid(column=2, row=1)

calc = tkinter.Button(text="Calculate", command=calculate)
calc.grid(column=1, row=2)

window.mainloop()
