# Define a sum function with two parameters and call the function.
def sum(a, b):
    return a + b

a = int(input('Enter 1st Number: '))
b = int(input('Enter 2nd Number: '))
print('Sum of {} and {} = {}'.format(a, b, sum(a, b)))
