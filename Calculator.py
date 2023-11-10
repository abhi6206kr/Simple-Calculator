import tkinter as tk

class Calculator:
    def __init__(self, master):
        self.master = master
        self.master.title("Simple Calculator")

        self.result_var = tk.StringVar()
        self.create_widgets()

    def create_widgets(self):
        # Entry widget to display the result
        entry = tk.Entry(self.master, textvariable=self.result_var, justify="right", font=('Arial', 14))
        entry.grid(row=0, column=0, columnspan=4, sticky="nsew")

        # Buttons for digits and operations
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+'
        ]

        # Set row and column weights to make the buttons expand with window resizing
        row_val = 1
        col_val = 0
        for button_text in buttons:
            tk.Button(self.master, text=button_text, command=lambda text=button_text: self.on_button_click(text)).grid(row=row_val, column=col_val, sticky="nsew")
            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1

        # Set row and column weights to make the buttons expand with window resizing
        for i in range(1, 5):
            self.master.grid_rowconfigure(i, weight=1)
            self.master.grid_columnconfigure(i, weight=1)

    def on_button_click(self, text):
        if text == "=":
            try:
                result = eval(self.result_var.get())
                self.result_var.set(result)
            except Exception as e:
                self.result_var.set("Error")
        else:
            current_text = self.result_var.get()
            new_text = current_text + text
            self.result_var.set(new_text)


if __name__ == "__main__":
    root = tk.Tk()
    calculator = Calculator(root)
    root.mainloop()
