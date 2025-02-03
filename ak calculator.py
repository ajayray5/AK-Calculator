import tkinter as tk
from tkinter import messagebox
import math

class AKCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("AK Calculator")
        self.root.geometry("400x600")
        self.root.resizable(True, True)
        
        self.theme = "light"
        self.create_widgets()
        self.bind_keys()

    def create_widgets(self):
        self.display = tk.Entry(self.root, font=("Arial", 24), borderwidth=2, relief="solid")
        self.display.grid(row=0, column=0, columnspan=4, sticky="nsew")

        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+',
            'C', '√', 'x²', 'x³',
            'sin', 'cos', 'tan', 'log',
            '!', '%', '|x|', 'x^y',
            'Light/Dark'
        ]

        row_val = 1
        col_val = 0
        for button in buttons:
            action = lambda x=button: self.click_event(x)
            tk.Button(self.root, text=button, width=5, height=2, command=action).grid(row=row_val, column=col_val, sticky="nsew")
            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1

        for i in range(5):
            self.root.grid_rowconfigure(i, weight=1)
            self.root.grid_columnconfigure(i, weight=1)

    def bind_keys(self):
        self.root.bind("<Return>", lambda event: self.click_event('='))
        self.root.bind("<BackSpace>", lambda event: self.click_event('C'))
        for key in '0123456789+-*/.':
            self.root.bind(key, lambda event, char=key: self.click_event(char))

    def click_event(self, key):
        if key == '=':
            try:
                result = str(eval(self.display.get()))
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, result)
            except Exception as e:
                messagebox.showerror("Error", "Invalid Input")
        elif key == 'C':
            self.display.delete(0, tk.END)
        elif key == '√':
            try:
                result = str(math.sqrt(float(self.display.get())))
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, result)
            except Exception as e:
                messagebox.showerror("Error", "Invalid Input")
        elif key == 'x²':
            try:
                result = str(float(self.display.get()) ** 2)
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, result)
            except Exception as e:
                messagebox.showerror("Error", "Invalid Input")
        elif key == 'x³':
            try:
                result = str(float(self.display.get()) ** 3)
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, result)
            except Exception as e:
                messagebox.showerror("Error", "Invalid Input")
        elif key == 'sin':
            try:
                result = str(math.sin(math.radians(float(self.display.get()))))
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, result)
            except Exception as e:
                messagebox.showerror("Error", "Invalid Input")
        elif key == 'cos':
            try:
                result = str(math.cos(math.radians(float(self.display.get()))))
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, result)
            except Exception as e:
                messagebox.showerror("Error", "Invalid Input")
        elif key == 'tan':
            try:
                result = str(math.tan(math.radians(float(self.display.get()))))
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, result)
            except Exception as e:
                messagebox.showerror("Error", "Invalid Input")
        elif key == 'log':
            try:
                result = str(math.log10(float(self.display.get())))
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, result)
            except Exception as e:
                messagebox.showerror("Error", "Invalid Input")
        elif key == '!':
            try:
                result = str(math.factorial(int(self.display.get())))
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, result)
            except Exception as e:
                messagebox.showerror("Error", "Invalid Input")
        elif key == '%':
            try:
                result = str(float(self.display.get()) / 100)
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, result)
            except Exception as e:
                messagebox.showerror("Error", "Invalid Input")
        elif key == '|x|':
            try:
                result = str(abs(float(self.display.get())))
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, result)
            except Exception as e:
                messagebox.showerror("Error", "Invalid Input")
        elif key == 'x^y':
            self.display.insert(tk.END, '**')
        elif key == 'Light/Dark':
            self.toggle_theme()
        else:
            self.display.insert(tk.END, key)

    def toggle_theme(self):
        if self.theme == "light":
            self.root.configure(bg="black")
            self.display.configure(bg="black", fg="white")
            self.theme = "dark"
        else:
            self.root.configure(bg="white")
            self.display.configure(bg="white", fg="black")
            self.theme = "light"

if __name__ == "__main__":
    root = tk.Tk()
    calculator = AKCalculator(root)
    root.mainloop()