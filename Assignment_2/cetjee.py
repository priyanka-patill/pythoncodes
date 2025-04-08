# Define sets of students enrolled in different entrance exams
cet_students = {'Alice', 'Bob', 'Charlie', 'David'}
jee_students = {'Eve', 'Frank', 'Charlie', 'David'}
neet_students = {'Grace', 'Heidi', 'Charlie', 'David'}

# Union: Students who are enrolled in any of the exams
all_students = cet_students.union(jee_students).union(neet_students)
print("Students enrolled in any exam (CET, JEE, NEET):")
print(all_students)

# Intersection: Students who are enrolled in all the exams
common_students = cet_students.intersection(jee_students).intersection(neet_students)
print("\nStudents enrolled in all exams (CET, JEE, NEET):")
print(common_students)

# Difference: Students who are enrolled in CET but not in JEE
cet_not_jee = cet_students.difference(jee_students)
print("\nStudents enrolled in CET but not in JEE:")
print(cet_not_jee)

# Difference: Students who are enrolled in JEE but not in NEET
jee_not_neet = jee_students.difference(neet_students)
print("\nStudents enrolled in JEE but not in NEET:")
print(jee_not_neet)

# Difference: Students who are enrolled in NEET but not in CET
neet_not_cet = neet_students.difference(cet_students)
print("\nStudents enrolled in NEET but not in CET:")
print(neet_not_cet)

# Symmetric Difference: Students who are enrolled in CET or JEE, but not both
cet_jee_diff = cet_students.symmetric_difference(jee_students)
print("\nStudents enrolled in CET or JEE, but not both:")
print(cet_jee_diff)

# Symmetric Difference: Students who are enrolled in JEE or NEET, but not both
jee_neet_diff = jee_students.symmetric_difference(neet_students)
print("\nStudents enrolled in JEE or NEET, but not both:")
print(jee_neet_diff)

# Symmetric Difference: Students who are enrolled in CET or NEET, but not both
cet_neet_diff = cet_students.symmetric_difference(neet_students)
print("\nStudents enrolled in CET or NEET, but not both:")
print(cet_neet_diff)
