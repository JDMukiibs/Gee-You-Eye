from tkinter import *
# from tkinter import messagebox


class Calculator(Frame):

    def __init__(self):
        Frame.__init__(self)
        self.master.title("Calculator")
        self.master.geometry("400x200")
        self.master.rowconfigure(0, weight=1)
        self.master.columnconfigure(0, weight=1)
        self.grid(sticky=W+E+N+S)

        # Make rows and columns expandable
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.columnconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)
        self.columnconfigure(2, weight=1)
        self.rowconfigure(3, weight=1)
        self.columnconfigure(3, weight=1)
        self.rowconfigure(4, weight=1)
        self.rowconfigure(5, weight=1)

        self.text1 = Entry(self, name="text1")
        # self.text1.insert(INSERT, "0")
        # Entry field will span 1 row and all columns
        self.text1.grid(row=0, column=0, columnspan=4, sticky=W+E+N+S)
        self.text1.rowconfigure(0, weight=1)
        self.text1.columnconfigure(0, weight=1)

        # Now we place the buttons top to bottom and they will be placed in the content frame
        self.button7 = Button(self, text="7", command=self.clickbutton7)
        self.button7.bind("<Enter>", self.rolloverEnter)
        self.button7.bind("<Leave>", self.rolloverLeave)
        self.button7.grid(row=1, column=0, sticky=W+E+N+S)

        self.button8 = Button(self, text="8", command=self.clickbutton8)
        self.button8.bind("<Enter>", self.rolloverEnter)
        self.button8.bind("<Leave>", self.rolloverLeave)
        self.button8.grid(row=1, column=1, sticky=W+E+N+S)

        self.button9 = Button(self, text="9", command=self.clickbutton9)
        self.button9.bind("<Enter>", self.rolloverEnter)
        self.button9.bind("<Leave>", self.rolloverLeave)
        self.button9.grid(row=1, column=2, sticky=W+E+N+S)

        self.divide = Button(self, text="/", command=self.clickbuttondiv)
        self.divide.bind("<Enter>", self.rolloverEnter)
        self.divide.bind("<Leave>", self.rolloverLeave)
        self.divide.grid(row=1, column=3, sticky=W+E+N+S)

        self.button4 = Button(self, text="4", command=self.clickbutton4)
        self.button4.bind("<Enter>", self.rolloverEnter)
        self.button4.bind("<Leave>", self.rolloverLeave)
        self.button4.grid(row=2, column=0, sticky=W+E+N+S)

        self.button5 = Button(self, text="5", command=self.clickbutton5)
        self.button5.bind("<Enter>", self.rolloverEnter)
        self.button5.bind("<Leave>", self.rolloverLeave)
        self.button5.grid(row=2, column=1, sticky=W+E+N+S)

        self.button6 = Button(self, text="6", command=self.clickbutton6)
        self.button6.bind("<Enter>", self.rolloverEnter)
        self.button6.bind("<Leave>", self.rolloverLeave)
        self.button6.grid(row=2, column=2, sticky=W+E+N+S)

        self.multiply = Button(self, text="*", command=self.clickbuttonmul)
        self.multiply.bind("<Enter>", self.rolloverEnter)
        self.multiply.bind("<Leave>", self.rolloverLeave)
        self.multiply.grid(row=2, column=3, sticky=W+E+N+S)

        self.button1 = Button(self, text="1", command=self.clickbutton1)
        self.button1.bind("<Enter>", self.rolloverEnter)
        self.button1.bind("<Leave>", self.rolloverLeave)
        self.button1.grid(row=3, column=0, sticky=W+E+N+S)

        self.button2 = Button(self, text="2", command=self.clickbutton2)
        self.button2.bind("<Enter>", self.rolloverEnter)
        self.button2.bind("<Leave>", self.rolloverLeave)
        self.button2.grid(row=3, column=1, sticky=W+E+N+S)

        self.button3 = Button(self, text="3", command=self.clickbutton3)
        self.button3.bind("<Enter>", self.rolloverEnter)
        self.button3.bind("<Leave>", self.rolloverLeave)
        self.button3.grid(row=3, column=2, sticky=W+E+N+S)

        self.subtract = Button(self, text="-", command=self.clickbuttonsub)
        self.subtract.bind("<Enter>", self.rolloverEnter)
        self.subtract.bind("<Leave>", self.rolloverLeave)
        self.subtract.grid(row=3, column=3, sticky=W+E+N+S)

        self.button0 = Button(self, text="0", command=self.clickbutton0)
        self.button0.bind("<Enter>", self.rolloverEnter)
        self.button0.bind("<Leave>", self.rolloverLeave)
        self.button0.grid(row=4, column=0, sticky=W+E+N+S)

        self.f_point = Button(self, text=".", command=self.clickbuttonfloat)
        self.f_point.bind("<Enter>", self.rolloverEnter)
        self.f_point.bind("<Leave>", self.rolloverLeave)
        self.f_point.grid(row=4, column=1, sticky=W+E+N+S)

        self.equals = Button(self, text="=", command=self.clickbuttonequals)
        self.equals.bind("<Enter>", self.rolloverEnter)
        self.equals.bind("<Leave>", self.rolloverLeave)
        self.equals.grid(row=4, column=2, sticky=W+E+N+S)

        self.add = Button(self, text="+", command=self.clickbuttonadd)
        self.add.bind("<Enter>", self.rolloverEnter)
        self.add.bind("<Leave>", self.rolloverLeave)
        self.add.grid(row=4, column=3, sticky=W+E+N+S)

        # Button to reset result and start calculating again
        self.reset = Button(self, text="Reset", command=self.clickreset)
        self.reset.bind("<Enter>", self.rolloverEnter)
        self.reset.bind("<Leave>", self.rolloverLeave)
        self.reset.grid(row=5, column=0, columnspan=4, sticky=W+E+N+S)

        self.result = ""  # value will be used to keep track of the buttons pressed

    def clickbutton0(self):
        self.result += "0"
        self.text1.insert(INSERT, self.button0['text'])

    def clickbutton1(self):
        self.result += "1"
        self.text1.insert(INSERT, self.button1['text'])

    def clickbutton2(self):
        self.result += "2"
        self.text1.insert(INSERT, self.button2['text'])

    def clickbutton3(self):
        self.result += "3"
        self.text1.insert(INSERT, self.button3['text'])

    def clickbutton4(self):
        self.result += "4"
        self.text1.insert(INSERT, self.button4['text'])

    def clickbutton5(self):
        self.result += "5"
        self.text1.insert(INSERT, self.button5['text'])

    def clickbutton6(self):
        self.result += "6"
        self.text1.insert(INSERT, self.button6['text'])

    def clickbutton7(self):
        self.result += "7"
        self.text1.insert(INSERT, self.button7['text'])

    def clickbutton8(self):
        self.result += "8"
        self.text1.insert(INSERT, self.button8['text'])

    def clickbutton9(self):
        self.result += "9"
        self.text1.insert(INSERT, self.button9['text'])

    def clickbuttondiv(self):
        self.result += "/"
        self.text1.delete(0, END)

    def clickbuttonmul(self):
        self.result += "*"
        self.text1.delete(0, END)

    def clickbuttonsub(self):
        self.result += "-"
        self.text1.delete(0, END)

    def clickbuttonadd(self):
        self.result += "+"
        self.text1.delete(0, END)

    def clickbuttonequals(self):
        self.text1.delete(0, END)
        self.text1.insert(INSERT, str(eval(self.result)))

    def clickbuttonfloat(self):
        self.result += "."
        self.text1.insert(INSERT, self.f_point['text'])

    def clickreset(self):
        self.text1.delete(0, END)
        self.result = ""

    def rolloverEnter(self, event):
        event.widget.config(relief=GROOVE)

    def rolloverLeave(self, event):
        event.widget.config(relief=RAISED)


if __name__ == "__main__":
    Calculator().mainloop()
