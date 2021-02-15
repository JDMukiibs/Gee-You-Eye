from tkinter import *
from tkinter import messagebox


class TemperatureConvert(Frame):

    def __init__(self):
        Frame.__init__(self)
        self.master.title("Fahrenheit -> Celsius")
        # self.master.geometry("200x200")
        self.pack()

        # Label component for Frame
        self.Label1 = Label(self, text="Fahrenheit: ")
        self.Label1.pack(side=LEFT)

        # Entry component
        self.frame1 = Frame(self)
        self.frame1.pack(side=LEFT, padx=5, pady=5)

        self.text1 = Entry(self.frame1, name="text1")
        self.text1.insert(INSERT, "Enter value here")
        self.text1.pack(side=LEFT, padx=5, pady=5)

        # Button component placed to right
        self.Button1 = Button(self, text="Convert to Celsius", command=self.clickbutton)
        self.Button1.bind("<Enter>", self.rolloverEnter)
        self.Button1.bind("<Leave>", self.rolloverLeave)
        self.Button1.pack(side=RIGHT, padx=5, pady=5)

    def clickbutton(self):
        contents = float(self.text1.get())
        result = 5/9 * (contents - 32)
        messagebox.showinfo("Celsius Equivalent", "{:.2f} Fahrenheit = {:.2f} Celsius".format(contents, result))

    @staticmethod
    def rolloverEnter(event):
        event.widget.config(relief=GROOVE)

    @staticmethod
    def rolloverLeave(event):
        event.widget.config(relief=RAISED)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    TemperatureConvert().mainloop()
