
from breezypythongui import EasyFrame

class Billing(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self, title="Billing System")
        self.addLabel(text="Item Price:", row=0, column=0)
        self.price = self.addFloatField(value=0.0, row=0, column=1)
        self.addLabel(text="Quantity:", row=1, column=0)
        self.qty = self.addIntegerField(value=0, row=1, column=1)
        self.addButton(text="Generate Bill", row=2, column=0, columnspan=2, command=self.bill)
        self.result = self.addLabel(text="", row=3, column=0, columnspan=2)

    def bill(self):
        total = self.price.getNumber() * self.qty.getNumber()
        if total > 1000:
            total *= 0.9
        self.result["text"] = f"Final Amount: {total:.2f}"

Billing().mainloop()
