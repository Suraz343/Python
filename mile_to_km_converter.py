from tkinter import *
window = Tk()
window.title("mile to KM converter")
window.minsize(height=250, width=300)

def miles_to_km():
    miles_input = input.get()
    km_value = int(1.609 * float(miles_input))
    text4.config(text=km_value)
    return km_value

input = Entry(width=15)
input.grid(row=3, column=3)
text1 = Label(text="Miles")
text1.grid(row=3, column=5)
text2 = Label(text="is equal to")
text2.grid(row=5, column=0)
text3 = Label(text="KM")
text3.grid(row=5, column=5)

text4 = Label(text=0)
text4.grid(row=5, column=3)
button = Button(text="Calculate", command=miles_to_km)
button.grid(row=9, column=3)

window.mainloop()