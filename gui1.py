import tkinter as tk
from tkinter import messagebox

# Function to add two numbers and display the result
def add_numbers():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        result = num1 + num2
        messagebox.showinfo("Result", f"The sum is: {result}")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numbers.")

# Create the main window
root = tk.Tk()
root.title("Add Two Numbers")

# Create and place the widgets
label1 = tk.Label(root, text="Enter first number:")
label1.pack()

entry1 = tk.Entry(root)
entry1.pack()

label2 = tk.Label(root, text="Enter second number:")
label2.pack()

entry2 = tk.Entry(root)
entry2.pack()

add_button = tk.Button(root, text="Add", command=add_numbers)
add_button.pack()

# Start the main event loop
root.mainloop()
