# To solve the quadratic equation.
a = int(input('Enter the coefficient of x^2: '))
b = int(input('Enter the coefficient of x: '))
c = int(input('Enter the last term: '))
d = b ** 2 - 4 * a * c
root1 = -b + d ** 0.5 / 2 * a
root2 = -b - d ** 0.5 / 2 * a
if d > 0: # Real and Unequal Roots
    print('Real and Unequal Roots:-')
    print('Root 1: ', root1, '\nRoot 2: ', root2)
elif d == 0: # Real and Equal Roots
    print('Real and Equal Roots:-')
    print('Root 1: ', root1, '\nRoot 2: ', root2)
else: # Imaginary Roots
    print('Imaginary Roots:-')
    print('Root 1: ', root1, '\nRoot 2: ', root2)    
    
