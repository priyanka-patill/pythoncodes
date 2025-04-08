import tkinter as tk
from tkinter import ttk

def convert():
    input_value = float(entry.get())
    conversion_type = conversion_var.get()

    if conversion_type == "Rupees to Dollars":
        result = input_value * 0.012  # Example conversion rate
    elif conversion_type == "Celsius to Fahrenheit":
        result = (input_value * 9/5) + 32
    elif conversion_type == "Inches to Feet":
        result = input_value / 12
    else:
        result = "Invalid conversion"

    result_label.config(text=f"Result: {result}")

# Create the main window
window = tk.Tk()
window.title("Unit Converter")

# Create input field
entry_label = tk.Label(window, text="Enter value:")
entry_label.grid(row=0, column=0, padx=10, pady=10)
entry = tk.Entry(window)
entry.grid(row=0, column=1, padx=10, pady=10)

# Create conversion type dropdown menu
conversion_var = tk.StringVar(value="Select conversion")
conversion_menu = ttk.Combobox(window, textvariable=conversion_var, state="readonly")
conversion_menu["values"] = ("Rupees to Dollars", "Celsius to Fahrenheit", "Inches to Feet")
conversion_menu.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

# Create convert button
convert_button = tk.Button(window, text="Convert", command=convert)
convert_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

# Create result label
result_label = tk.Label(window, text="Result: ")
result_label.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

# Run the application
window.mainloop()
