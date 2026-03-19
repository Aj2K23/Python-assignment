

from breezypythongui import EasyFrame
from tkinter import messagebox

class Calculator(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self, title="Calculator")
        self.addLabel(text="Number 1:", row=0, column=0)
        self.num1 = self.addIntegerField(value=0, row=0, column=1)
        self.addLabel(text="Number 2:", row=1, column=0)
        self.num2 = self.addIntegerField(value=0, row=1, column=1)
        self.result = self.addFloatField(value=0.0, row=2, column=1, precision=2, state="readonly")

        self.addButton(text="Add", row=3, column=0, command=lambda: self.calculate("add"))
        self.addButton(text="Subtract", row=3, column=1, command=lambda: self.calculate("sub"))
        self.addButton(text="Multiply", row=4, column=0, command=lambda: self.calculate("mul"))
        self.addButton(text="Divide", row=4, column=1, command=lambda: self.calculate("div"))

    def calculate(self, op):
        try:
            a = self.num1.getNumber()
            b = self.num2.getNumber()
            if op == "add":
                self.result.setNumber(a + b)
            elif op == "sub":
                self.result.setNumber(a - b)
            elif op == "mul":
                self.result.setNumber(a * b)
            elif op == "div":
                self.result.setNumber(a / b)
        except ZeroDivisionError:
            messagebox.showerror("Error", "Cannot divide by zero")

Calculator().mainloop()
     
