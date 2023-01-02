import tkinter

window = tkinter.Tk()
window.title('Miles to KM converter')
window.minsize(500, 300)
window.config(padx=20, pady=20)

input_entry = tkinter.Entry(width=15)
input_entry.grid(column=1, row=0)

miles_label = tkinter.Label(text='Miles')
miles_label.grid(column=2, row=0)
miles_label.config(pady=10)

text_label = tkinter.Label(text='is equals to')
text_label.grid(column=0, row=1)
text_label.config(pady=10)

convert_label = tkinter.Label(text='0')
convert_label.grid(column=1, row=1)
convert_label.config(pady=10)

km_label = tkinter.Label(text='Km')
km_label.grid(column=2, row=1)


def button_click():
    value_in_miles = input_entry.get()
    value_in_km = float(value_in_miles) * 1.609344
    convert_label.config(text=round(value_in_km))


cal_button = tkinter.Button(text='Calculate', command=button_click)
cal_button.grid(column=1, row=2)

window.mainloop()

