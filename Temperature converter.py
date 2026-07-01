import tkinter


def convert(out_data, temp_data):
    """Convert temperature from Fahrenheit to Celsius."""

    fahrenheit = temp_data.get()
    celsius = (fahrenheit - 32) * 5 / 9
    out_data.set(f"{celsius:.2f}")


window = tkinter.Tk()

frame = tkinter.Frame(window)
frame.pack()

out_data = tkinter.StringVar()
temp_data = tkinter.DoubleVar()

tkinter.Label(frame, text="Temperature in Fahrenheit:").pack()

text = tkinter.Entry(frame, textvariable=temp_data)
text.pack()

label = tkinter.Label(frame, textvariable=out_data)
label.pack()

button = tkinter.Button(
    frame,
    text="Convert",
    command=lambda: convert(out_data, temp_data)
)
button.pack()

button2 = tkinter.Button(
    frame,
    text="Quit",
    command=window.destroy
)
button2.pack()

window.mainloop()
