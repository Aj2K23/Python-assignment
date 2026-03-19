from breezypythongui import EasyFrame
from tkinter import messagebox

class TempConverter(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self, title="Temperature Converter")
        self.addLabel(text="Celsius:", row=0, column=0)
        self.celsius = self.addFloatField(value=0.0, row=0, column=1)
        self.addButton(text="Convert", row=1, column=0, columnspan=2, command=self.convert)
        self.addLabel(text="Fahrenheit:", row=2, column=0)
        self.fahrenheit = self.addFloatField(value=0.0, row=2, column=1, precision=2, state="readonly")

    def convert(self):
        try:
            c = self.celsius.getNumber()
            f = (c * 9/5) + 32
            self.fahrenheit.setNumber(f)
        except Exception:
            messagebox.showerror("Error", "Invalid input")

TempConverter().mainloop()
