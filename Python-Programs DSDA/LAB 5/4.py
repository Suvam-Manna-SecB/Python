'''
Create a set given below
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]
I. Find the length of the set it_companies
II. Add &#39;Twitter&#39; to it_companies
III. Insert multiple IT companies at once to the set it_companies
IV. Remove one of the companies from the set it_companies
V. What is the difference between remove and discard
'''

it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

length_it_companies = len(it_companies)
print(f"Length of it_companies: {length_it_companies}")

it_companies.add('Twitter')
print(f"it_companies after adding 'Twitter': {it_companies}")

more_companies = {'Intel', 'Nvidia', 'Salesforce'}
it_companies.update(more_companies)
print(f"it_companies after adding multiple companies: {it_companies}")

it_companies.remove('Twitter')
print(f"it_companies after removing 'Twitter': {it_companies}")

try:
    it_companies.remove('NonExistentCompany')
except KeyError as e:
    print(f"remove() raised an error: {e}")

it_companies.discard('NonExistentCompany')
print("discard() did not raise an error")
