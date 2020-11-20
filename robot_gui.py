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
        ser.write(b'I'+i+b'\r\n')

    if axis == 2:
        i = str.encode(txt2.get())
        ser.write(b'J'+i+b'\r\n')

    if axis == 3:
        x = str.encode(txtX.get())
        y = str.encode(txtY.get())
        ser.write(b'X'+x+b' Y'+y+b'\r\n')

    readedText = ser.readline()
    readedText = ser.readline()

    ser.close()

    res = readedText.rstrip("\r\n")
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

def clickedXY():

    devWrite(3)

def clickedDownX():

    i_str = txtX.get()
    i_float = float(i_str)
    i_float-=1.0
    i_str = str(i_float)
    txtX.delete(0,END)
    txtX.insert(0,i_str)

    devWrite(3)

def clickedUpX():

    i_str = txtX.get()
    i_float = float(i_str)
    i_float+=1.0
    i_str = str(i_float)
    txtX.delete(0,END)
    txtX.insert(0,i_str)

    devWrite(3)

def clickedDownY():

    i_str = txtY.get()
    i_float = float(i_str)
    i_float-=1.0
    i_str = str(i_float)
    txtY.delete(0,END)
    txtY.insert(0,i_str)

    devWrite(3)

def clickedUpY():

    i_str = txtY.get()
    i_float = float(i_str)
    i_float+=1.0
    i_str = str(i_float)
    txtY.delete(0,END)
    txtY.insert(0,i_str)

    devWrite(3)


window = Tk()

window.geometry('700x200')

window.title("Robot app")

lbl = Label(window, text="Hello", font=("Arial Bold", 20))
lbl.grid(column=0, columnspan=5, row=0)

btn = Button(window, text="Start", command=clickedStart)
btn.grid(column=5, row=0)

txt1 = Entry(window, width=10)
txt1.grid(column=1, row=1)
txt1.delete(0,END)
txt1.insert(0,"25")

btn1d = Button(window, text="Down", command=clickedDown1)
btn1d.grid(column=2, row=1)

btn1u = Button(window, text="Up", command=clickedUp1)
btn1u.grid(column=3, row=1)

txt2 = Entry(window, width=10)
txt2.grid(column=1, row=2)
txt2.delete(0,END)
txt2.insert(0,"105")

btn2d = Button(window, text="Down", command=clickedDown2)
btn2d.grid(column=2, row=2)

btn2u = Button(window, text="Up", command=clickedUp2)
btn2u.grid(column=3, row=2)

txtX = Entry(window, width=10)
txtX.grid(column=1, row=3)
txtX.delete(0,END)
txtX.insert(0,"40")

txtY = Entry(window, width=10)
txtY.grid(column=2, row=3)
txtY.delete(0,END)
txtY.insert(0,"0")

btn1 = Button(window, text="XY", command=clickedXY)
btn1.grid(column=3, row=3)

btn3d = Button(window, text="X Down", command=clickedDownX)
btn3d.grid(column=4, row=3)

btn3u = Button(window, text="X Up", command=clickedUpX)
btn3u.grid(column=5, row=3)

btn4d = Button(window, text="Y Down", command=clickedDownY)
btn4d.grid(column=4, row=4)

btn4u = Button(window, text="Y Up", command=clickedUpY)
btn4u.grid(column=5, row=4)

txt1.focus()
window.mainloop()
