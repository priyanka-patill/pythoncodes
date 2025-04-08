students = [
    {"Name": "Alice", "Grade": 85, "Attendance": 90},
    {"Name": "Bob", "Grade": 78, "Attendance": 85},
    {"Name": "Charlie", "Grade": 92, "Attendance": 95},
    {"Name": "Diana", "Grade": 88, "Attendance": 80},
]

# Sorting the list of dictionaries based on the 'Grade' key using a lambda function
sorted_students = sorted(students, key=lambda x: x["Grade"],reverse=True)

# Printing the sorted list of dictionaries
for student in sorted_students:
    print(f"Name: {student['Name']}, Grade: {student['Grade']}")
print("----------------------------------------------------------------------------------------------------------------------------")
print("----------------------------------------------------------------------------------------------------------------------------")
print("----------------------------------------------------------------------------------------------------------------------------")
print("----------------------------------------------------------------------------------------------------------------------------")

# Sorting the list of dictionaries based on the 'Attendance' key using a lambda function
sorted_students = sorted(students, key=lambda x: x["Attendance"], reverse=True)

# Printing the sorted list of dictionaries
for student in sorted_students:
    print(f"Name: {student['Name']},  Attendance: {student['Attendance']}")


