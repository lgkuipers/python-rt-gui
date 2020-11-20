from tkinter import Tk, Label, Button, W

class MyFirstGUI:
    def __init__(self, master):
        self.master = master
        master.title("A simple GUI")
        
        self.label = Label(master, text="This is our first GUI!")
        self.greet_button = Button(master, text="Greet", command=self.greet)
        self.close_button = Button(master, text="Close", command=master.quit)

        self.label.grid(columnspan=2, sticky=W)
        self.greet_button.grid(row=1)
        self.close_button.grid(row=1, column=1)

    def greet(self):
        print("Greetings!")

root = Tk()
my_gui = MyFirstGUI(root)
root.mainloop()
