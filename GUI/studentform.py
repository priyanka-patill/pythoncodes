import tkinter as tk
from tkinter import messagebox

# Function to handle form submission
def submit_form():
    name = name_var.get()
    age = age_var.get()
    gender = gender_var.get()
    course = course_var.get()
    email = email_var.get()
    
    if name and age and gender and course and email:
        messagebox.showinfo("Form Submitted", f"Thank you, {name}! Your data has been recorded.")
        # Here, you can add logic to save the data (e.g., in a file or database)
    else:
        messagebox.showwarning("Incomplete Form", "Please fill in all the fields!")

# Create the main window
root = tk.Tk()
root.title("Student Registration Form")

# Variables to store form input
name_var = tk.StringVar()
age_var = tk.StringVar()
gender_var = tk.StringVar()
course_var = tk.StringVar()
email_var = tk.StringVar()

# Create form labels and input fields
tk.Label(root, text="Student Registration Form", font=("Arial", 16, "bold")).grid(row=0, column=0, columnspan=2, pady=10)

tk.Label(root, text="Name:").grid(row=1, column=0, sticky="w", padx=10, pady=5)
tk.Entry(root, textvariable=name_var).grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="Age:").grid(row=2, column=0, sticky="w", padx=10, pady=5)
tk.Entry(root, textvariable=age_var).grid(row=2, column=1, padx=10, pady=5)

tk.Label(root, text="Gender:").grid(row=3, column=0, sticky="w", padx=10, pady=5)
tk.Radiobutton(root, text="Male", value="Male", variable=gender_var).grid(row=3, column=1, sticky="w", padx=10)
tk.Radiobutton(root, text="Female", value="Female", variable=gender_var).grid(row=4, column=1, sticky="w", padx=10)

tk.Label(root, text="Course:").grid(row=5, column=0, sticky="w", padx=10, pady=5)
tk.Entry(root, textvariable=course_var).grid(row=5, column=1, padx=10, pady=5)

tk.Label(root, text="Email:").grid(row=6, column=0, sticky="w", padx=10, pady=5)
tk.Entry(root, textvariable=email_var).grid(row=6, column=1, padx=10, pady=5)

# Submit button
tk.Button(root, text="Submit", command=submit_form, bg="blue", fg="white").grid(row=7, column=0, columnspan=2, pady=10)

# Start the main event loop
root.mainloop()
