# Example of a nested dictionary
student_data = {
    'student1': {
        'name': 'John',
        'age': 20,
        'courses': ['Math', 'Science']
    },
    'student2': {
        'name': 'Alice',
        'age': 22,
        'courses': ['English', 'History']
    }
}

print(student_data)

# Accessing data in a nested dictionary

# Get the name of student1
name_student1 = student_data['student1']['name']
print(f'Name of student1: {name_student1}')

# Get the age of student2
age_student2 = student_data['student2']['age']
print(f'Age of student2: {age_student2}')

# Get the courses of student1
courses_student1 = student_data['student1']['courses']
print(f'Courses of student1: {courses_student1}')

# Updating data in a nested dictionary

# Update the age of student1
student_data['student1']['age'] = 21

# Add a new course to student2
student_data['student2']['courses'].append('Art')

print(student_data)

