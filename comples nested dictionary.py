# Example of a more complex nested dictionary
company = {
    'sales': {
        'department_head': 'Emma',
        'employees': {
            'emp1': {'name': 'John', 'age': 30, 'position': 'Manager'},
            'emp2': {'name': 'Linda', 'age': 28, 'position': 'Sales Associate'}
        }
    },
    'hr': {
        'department_head': 'David',
        'employees': {
            'emp1': {'name': 'Alice', 'age': 35, 'position': 'HR Manager'},
            'emp2': {'name': 'Bob', 'age': 25, 'position': 'Recruiter'}
        }
    }
}

print(company)

hr_head = company['hr']['department_head']
print(f'HR Department Head: {hr_head}')
sales_emp2_position = company['sales']['employees']['emp2']['position']
print(f'Sales Employee 2 Position: {sales_emp2_position}')

