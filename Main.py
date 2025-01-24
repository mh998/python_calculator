import tkinter as tk

def add():
    try:
        first_number = float(entry1.get())
        second_number = float(entry2.get())
        result.set(first_number + second_number)
    except ValueError:
        result.set("Error")

def subtract():
    try:
        first_number = float(entry1.get())
        second_number = float(entry2.get())
        result.set(first_number - second_number)
    except ValueError:
        result.set("Error")

def multiply():
    try:
        first_number = float(entry1.get())
        second_number = float(entry2.get())
        result.set(first_number * second_number)
    except ValueError:
        result.set("Error")

def divide():
    try:
        first_number = float(entry1.get())
        second_number = float(entry2.get())
        if second_number == 0:
            result.set("Error: Division by zero")
        else:
            result.set(first_number / second_number)
    except ValueError:
        result.set("Error")

# Create the main window
root = tk.Tk()
root.title("Simple Calculator")

# Create and set the variables for entry widgets and result display
entry1 = tk.Entry(root)
entry2 = tk.Entry(root)
result = tk.StringVar()

# Create and place the widgets in the window
entry1.grid(row=0, column=0, columnspan=4)
entry2.grid(row=1, column=0, columnspan=4)
tk.Label(root, text="Result:").grid(row=2, column=0)
tk.Entry(root, textvariable=result).grid(row=2, column=1, columnspan=3)

# Create and place the buttons in the window
tk.Button(root, text="Add", command=add).grid(row=3, column=0)
tk.Button(root, text="Subtract", command=subtract).grid(row=3, column=1)
tk.Button(root, text="Multiply", command=multiply).grid(row=3, column=2)
tk.Button(root, text="Divide", command=divide).grid(row=3, column=3)

# Start the main event loop
root.mainloop()