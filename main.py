from tkinter import *

window = Tk()
window.title("Miles to Km Converter")
window.minsize(width=300, height=200)
window.config(padx=20, pady=20)

def button_clicked():
    new_text = round(int(input.get()) * 1.609344)
    conversion_output_label.config(text=new_text)

#Label
conversion_label = Label(text="is equal to", font=("Arial", 24, "bold"))
conversion_label.grid(column=0, row=1)
conversion_label.config(padx=5, pady=5)


input_label = Label(text="Miles", font=("Arial", 24, "bold"))
input_label.grid(column=2, row=0)
input_label.config(padx=5, pady=5)


conversion_output_label = Label(text="0", font=("Arial", 24, "bold"))
conversion_output_label.grid(column=1, row=1)
conversion_output_label.config(padx=5, pady=5)


conversion_factor_label = Label(text="Km", font=("Arial", 24, "bold"))
conversion_factor_label.grid(column=2, row=1)
conversion_factor_label.config(padx=5, pady=5)


#Button
button = Button(text="Calculate", command=button_clicked)
button.grid(column=1, row=2)


#Entry
input = Entry(width=7)
print(input.get())
input.grid(column=1, row=0)


window.mainloop()