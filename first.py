from tkinter import *

def clicked():

    res = "Welcome " + txt.get()
    lbl.configure(text=res)


window = Tk()

window.geometry('350x200')

window.title("Welcome to LikeGeeks app")

lbl = Label(window, text="Hello", font=("Arial Bold", 50))
lbl.grid(column=0, row=0)

txt = Entry(window, width=10)
txt.grid(column=1, row=0)

btn = Button(window, text="Click Me", command=clicked)
btn.grid(column=2, row=0)


txt.focus()
window.mainloop()
