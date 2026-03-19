
from breezypythongui import EasyFrame
import re

class PasswordStrength(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self, title="Password Strength Checker")
        self.addLabel(text="Password:", row=0, column=0)
        self.pwd = self.addTextField(text="", row=0, column=1)
        self.pwd.config(show='*')
        self.addButton(text="Check Strength", row=1, column=0, columnspan=2, command=self.check)
        self.result = self.addLabel(text="", row=2, column=0, columnspan=2)

    def check(self):
        pwd = self.pwd.getText()
        strength = "Weak"
        if len(pwd) >= 8 and re.search(r"\d", pwd) and re.search(r"[!@#$%^&*]", pwd):
            strength = "Strong"
        elif len(pwd) >= 6 and re.search(r"\d", pwd):
            strength = "Moderate"
        self.result["text"] = strength

PasswordStrength().mainloop()
