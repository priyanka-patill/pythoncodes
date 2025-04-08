import tkinter as tk
from tkinter import messagebox

# Function to submit the form
def submit_form():
    name = entry_name.get()
    age = entry_age.get()
    gender = gender_var.get()
    course = course_var.get()
    
    if name and age and gender and course:
        messagebox.showinfo("Student Information", f"Name: {name}\nAge: {age}\nGender: {gender}\nCourse: {course}")
    else:
        messagebox.showerror("Error", "Please fill out all fields.")

# Create the main window
root = tk.Tk()
root.title("Student Form")

# Create and place the widgets
tk.Label(root, text="Name:").grid(row=0, column=0, padx=10, pady=10)
entry_name = tk.Entry(root)
entry_name.grid(row=0, column=1, padx=10, pady=10)

tk.Label(root, text="Age:").grid(row=1, column=0, padx=10, pady=10)
entry_age = tk.Entry(root)
entry_age.grid(row=1, column=1, padx=10, pady=10)

tk.Label(root, text="Gender:").grid(row=2, column=0, padx=10, pady=10)
gender_var = tk.StringVar()
tk.Radiobutton(root, text="Male", variable=gender_var, value="Male").grid(row=2, column=1, padx=10, pady=10)
tk.Radiobutton(root, text="Female", variable=gender_var, value="Female").grid(row=2, column=2, padx=10, pady=10)

tk.Label(root, text="Course:").grid(row=3, column=0, padx=10, pady=10)
course_var = tk.StringVar()
tk.OptionMenu(root, course_var, "Mathematics", "Science", "Arts", "Engineering").grid(row=3, column=1, padx=10, pady=10)

submit_button = tk.Button(root, text="Submit", command=submit_form)
submit_button.grid(row=4, columnspan=3, pady=20)

# Start the main event loop
root.mainloop()
