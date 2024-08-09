# Write a program to find roots of a quadratic equation.

a = int(input('Enter Coefficient of x^2: '))
b = int(input('Enter Coefficient of x: '))
c = int(input('Enter Coefficient of Last Term: '))

d = b*b - 4*a*c

if d > 0: # Real and Unequal Roots
    root1 = -b + d**0.5 / 2 * a
    root2 = -b - d**0.5 / 2 * a
    print('Real and Unqual Roots :-')
    print('Root 1: ', root1)
    print('Root 2: ', root2)
elif d == 0: # Real and Equal Roots
    root = -b + d**0.5 / 2 * a
    print('Real and Equal Roots :-')
    print('Root 1: ', root)
    print('Root 2: ', root)
else: # Imaginary Roots
    root1 = -b + d**0.5 / 2 * a
    root2 = -b - d**0.5 / 2 * a
    print('Complex Roots :-')
    print('Root 1: ', root1)
    print('Root 2: ', root2)
