import re
from tkinter import Tk, Label, Entry, Button, StringVar, messagebox

class PasswordStrengthTool:
    def __init__(self, master):
        self.master = master
        master.title("Password Strength Tool")

        self.label = Label(master, text="Enter a password to check its strength:")
        self.label.pack()

        self.password_var = StringVar()
        self.password_entry = Entry(master, textvariable=self.password_var, show='*')
        self.password_entry.pack()

        self.check_button = Button(master, text="Check Strength", command=self.check_strength)
        self.check_button.pack()

        self.result_label = Label(master, text="", fg="blue")
        self.result_label.pack()

    def check_strength(self):
        password = self.password_var.get()
        strength, feedback = self.evaluate_password(password)
        self.result_label.config(text=feedback)
        if strength == "Strong":
            self.result_label.config(fg="green")
        elif strength == "Moderate":
            self.result_label.config(fg="orange")
        else:
            self.result_label.config(fg="red")

    def evaluate_password(self, password):
        if len(password) < 8:
            return "Weak", "Password must be at least 8 characters long."

        criteria = {
            "length": len(password) >= 8,
            "uppercase": re.search(r'[A-Z]', password) is not None,
            "lowercase": re.search(r'[a-z]', password) is not None,
            "digit": re.search(r'\d', password) is not None,
            "special": re.search(r'[!@#$%^&*(),.?":{}|<>]', password) is not None
        }

        if all(criteria.values()):
            return "Strong", "Strong password!"
        elif sum(criteria.values()) >= 3:
            return "Moderate", "Moderate password. Consider adding more diverse characters."
        else:
            return "Weak", "Weak password. Improve by adding uppercase, lowercase letters, digits, and special characters."

def main():
    root = Tk()
    app = PasswordStrengthTool(root)
    root.mainloop()

if __name__ == "__main__":
    main()
