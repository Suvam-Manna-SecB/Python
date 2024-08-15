'''
Create a student dictionary and add first_name, last_name, gender, age, marital status, skills,
country, city and address as keys for the dictionary
I. Get the length of the student dictionary
II. Get the value of skills and check the data type, it should be a list
III. Modify the skills values by adding one or two skills
IV. Get the dictionary keys as a list
V. Get the dictionary values as a list
VI. Change the dictionary to a list of tuples using _items()_ method
VII. Delete one of the items in the dictionary
VIII. Delete one of the dictionaries
'''

student = {
    'first_name': 'John',
    'last_name': 'Doe',
    'gender': 'Male',
    'age': 20,
    'marital_status': 'Single',
    'skills': ['Python', 'Data Analysis'],
    'country': 'USA',
    'city': 'New York',
    'address': '123 Elm Street'
}

length_student = len(student)
print(f"Length of student dictionary: {length_student}")

skills = student['skills']
print(f"Skills: {skills}")
print(f"Data type of skills: {type(skills)}")

student['skills'].extend(['Machine Learning', 'Django'])
print(f"Updated skills: {student['skills']}")

keys_list = list(student.keys())
print(f"Dictionary keys: {keys_list}")

values_list = list(student.values())
print(f"Dictionary values: {values_list}")

items_list = list(student.items())
print(f"Dictionary items as list of tuples: {items_list}")

del student['address']
print(f"Dictionary after deleting 'address': {student}")

del student
