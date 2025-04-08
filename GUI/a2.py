import tkinter as tk

def calculate_area():
    figure_type = figure_var.get()
    try:
        if figure_type == "Circle":
            radius = float(entry1.get())
            result = 3.1416 * (radius ** 2)
        elif figure_type == "Rectangle":
            length = float(entry1.get())
            width = float(entry2.get())
            result = length * width
        elif figure_type == "Triangle":
            base = float(entry1.get())
            height = float(entry2.get())
            result = 0.5 * base * height
        else:
            result = "Invalid figure type"

        result_label.config(text=f"Area: {result:.2f}")

    except ValueError:
        result_label.config(text="Please enter valid numbers")

# Create the main window
window = tk.Tk()
window.title("Area Calculator")

# Create figure type dropdown menu
figure_label = tk.Label(window, text="Select Figure:")
figure_label.grid(row=0, column=0, padx=10, pady=10)
figure_var = tk.StringVar(value="Select")
figure_menu = tk.OptionMenu(window, figure_var, "Circle", "Rectangle", "Triangle")
figure_menu.grid(row=0, column=1, padx=10, pady=10)

# Create input fields
entry1_label = tk.Label(window, text="Enter dimension 1 (e.g., radius/length/base):")
entry1_label.grid(row=1, column=0, padx=10, pady=10)
entry1 = tk.Entry(window)
entry1.grid(row=1, column=1, padx=10, pady=10)

entry2_label = tk.Label(window, text="Enter dimension 2 (e.g., width/height, if needed):")
entry2_label.grid(row=2, column=0, padx=10, pady=10)
entry2 = tk.Entry(window)
entry2.grid(row=2, column=1, padx=10, pady=10)

# Create calculate button
calculate_button = tk.Button(window, text="Calculate", command=calculate_area)
calculate_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

# Create result label
result_label = tk.Label(window, text="Area: ")
result_label.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

# Run the application
window.mainloop()
