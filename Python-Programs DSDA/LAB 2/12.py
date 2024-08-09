# Write a program in python that prompts the user to input a number and
# prints its multiplication table.
n = int(input('Enter Number: '))
for i in range(1, 11):
    print('{} X {} = {}'.format(n, i, n*i))
