import tkinter

def check_metal(result, melting_temp):
    temperature = melting_temp.get()

    if temperature > 3000:
        result.set("This metal is suitable for incandescent filament")
    elif temperature >= 1000:
        result.set("This metal is suitable for incandescent filament, but efficiency is undefined")
    else:
        result.set("This metal is not suitable at all")


window = tkinter.Tk()

frame = tkinter.Frame(window)
frame.pack()

result = tkinter.StringVar()
melting_temp = tkinter.DoubleVar()

tkinter.Label(frame, text="Enter the melting temperature of your metal:").pack()

entry = tkinter.Entry(frame, textvariable=melting_temp)
entry.pack()

label = tkinter.Label(frame, textvariable=result)
label.pack()

button = tkinter.Button(
    frame,
    text="Check",
    command=lambda: check_metal(result, melting_temp)
)
button.pack()

quit_button = tkinter.Button(
    frame,
    text="Quit",
    command=window.destroy
)
quit_button.pack()

window.mainloop()
