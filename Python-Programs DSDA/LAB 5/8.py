'''
7.Create a person dictionary.
person={
'first_name': 'Asabeneh',
'last_name': 'Yetayeh',
'age': 250,
'country': 'Finland',
'is_marred': True,
'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
'address': {
'street': 'Space street',
'zipcode': '02210'
}
}
I. Check if the person dictionary has skills key, if so print out the middle skill in the skills list.
II. Check if the person dictionary has skills key, if so check if the person has 'Python' skill and
print out the result.
III. If a person skills has only JavaScript and React, print('He is a front end developer'), if the
person skills has Node, Python, MongoDB, print('He is a backend developer'), if the person
skills has React, Node and MongoDB, Print('He is a fullstack developer'), else print('unknown
title') - for more accurate results more conditions can be nested!
IV. If the person is married and if he lives in Finland, print the information in the following
format:

```py
Asabeneh Yetayeh lives in Finland. He is married.
``
'''


person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}

if 'skills' in person:
    skills_list = person['skills']
    middle_index = len(skills_list) // 2
    middle_skill = skills_list[middle_index]
    print(f"Middle skill: {middle_skill}")

if 'skills' in person:
    has_python = 'Python' in person['skills']
    print(f"Has Python skill: {has_python}")

skills = set(person['skills'])
if {'JavaScript', 'React'}.issubset(skills):
    print('He is a front end developer')
elif {'Node', 'Python', 'MongoDB'}.issubset(skills):
    print('He is a backend developer')
elif {'React', 'Node', 'MongoDB'}.issubset(skills):
    print('He is a fullstack developer')
else:
    print('unknown title')

if person.get('is_married') and person.get('country') == 'Finland':
    print(f"{person['first_name']} {person['last_name']} lives in Finland. He is married.")
