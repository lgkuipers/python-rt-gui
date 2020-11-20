from tkinter import *
import serial
import time

def devWrite(axis):

    ser=serial.Serial('/dev/ttyACM0',baudrate=115200, bytesize=8, parity='N', stopbits=1, timeout=None, xonxoff=0, rtscts=0)

    i = 25
    if axis == 0:
        ser.write(b'\r\n')

    if axis == 1:
        i = str.encode(txt1.get())
        ser.write(b'I'+i+'\r\n')

    if axis == 2:
        i = str.encode(txt2.get())
        ser.write(b'J'+i+'\r\n')

    readedText = ser.readline()
    readedText = ser.readline()

    ser.close()

    res = readedText
    lbl.configure(text=res)


def clickedStart():

    devWrite(0)

def clickedDown1():

    i_str = txt1.get()
    i_int = int(i_str)
    i_int-=1
    i_str = str(i_int)
    txt1.delete(0,END)
    txt1.insert(0,i_str)

    devWrite(1)

def clickedUp1():

    i_str = txt1.get()
    i_int = int(i_str)
    i_int+=1
    i_str = str(i_int)
    txt1.delete(0,END)
    txt1.insert(0,i_str)

    devWrite(1)

def clickedDown2():

    i_str = txt2.get()
    i_int = int(i_str)
    i_int-=1
    i_str = str(i_int)
    txt2.delete(0,END)
    txt2.insert(0,i_str)

    devWrite(2)

def clickedUp2():

    i_str = txt2.get()
    i_int = int(i_str)
    i_int+=1
    i_str = str(i_int)
    txt2.delete(0,END)
    txt2.insert(0,i_str)

    devWrite(2)



window = Tk()

window.geometry('700x200')

window.title("Robot app")

lbl = Label(window, text="Hello", font=("Arial Bold", 20))
lbl.grid(column=0, row=0)

btn = Button(window, text="Start", command=clickedStart)
btn.grid(column=1, row=0)

txt1 = Entry(window, width=10)
txt1.grid(column=1, row=1)
txt1.delete(0,END)
txt1.insert(0,"25")

btn1 = Button(window, text="Down", command=clickedDown1)
btn1.grid(column=2, row=1)

btn1 = Button(window, text="Up", command=clickedUp1)
btn1.grid(column=3, row=1)

txt2 = Entry(window, width=10)
txt2.grid(column=1, row=2)
txt2.delete(0,END)
txt2.insert(0,"105")

btn2 = Button(window, text="Down", command=clickedDown2)
btn2.grid(column=2, row=2)

btn2 = Button(window, text="Up", command=clickedUp2)
btn2.grid(column=3, row=2)

txt1.focus()
window.mainloop()
