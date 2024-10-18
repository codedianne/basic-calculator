import tkinter as tk


class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Simple Calculator")
        master.geometry("400x600")  # Set a fixed window size

        # Create entry to display the result
        self.result_var = tk.StringVar()
        self.entry = tk.Entry(master, textvariable=self.result_var, font=("Arial", 30), bd=10, insertwidth=4, width=14,
                              borderwidth=4, justify='right', bg="#f0f0f0")
        self.entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="nsew")

        # Button Layout
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            'C', '0', '=', '+'
        ]

        # Create buttons dynamically
        row_val = 1
        col_val = 0

        for button in buttons:
            self.create_button(button, row_val, col_val)
            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1

        # Configure grid weights for responsive design
        for i in range(5):
            master.grid_rowconfigure(i, weight=1)
            master.grid_columnconfigure(i, weight=1)

        # Bind keyboard events
        master.bind('<Key>', self.key_press)

    def create_button(self, text, row, column):
        button = tk.Button(self.master, text=text, font=("Arial", 18), bg="grey", fg="white",
                           command=lambda: self.on_button_click(text))
        button.grid(row=row, column=column, sticky="nsew", padx=5, pady=5)  # Make buttons fill their grid space

    def key_press(self, event):
        key = event.char
        if key in '0123456789+-*/':
            self.on_button_click(key)
        elif key == '\r':  # Enter key
            self.on_button_click('=')
        elif key == '\x08':  # Backspace key
            self.on_button_click('C')  # Use C to remove last character
        elif key == 'c':  # Clear (AC)
            self.on_button_click('AC')

    def on_button_click(self, char):
        current_text = self.result_var.get()

        # Check if the last character is an operator
        if char in "+-*/":
            if current_text and current_text[-1] in "+-*/":
                # Replace the last operator
                current_text = current_text[:-1]

        if char == 'C':
            self.result_var.set(current_text[:-1])  # Remove the last character
        elif char == 'AC':
            self.result_var.set("")  # Clear everything in the entry
        elif char == '=':
            try:
                # Evaluate the expression entered by the user
                result = eval(current_text)
                self.result_var.set(result)
            except Exception:
                self.result_var.set("Error")  # Show error if evaluation fails
        else:
            self.result_var.set(current_text + char)  # Append character to the entry


if __name__ == "__main__":
    root = tk.Tk()
    calculator = Calculator(root)

    # Configure grid weights for responsive design
    for i in range(5):
        root.grid_rowconfigure(i, weight=1)
        root.grid_columnconfigure(i, weight=1)

    root.mainloop()
