# Quadratic equation is calculated as follows: ax^2 + bx + c = 0. Write a
# function which calculates solution set of a quadratic equation.

def solveQuadraticEquation(a, b, c):
    d = b**2 - 4 * a * c
    root1 = -b + d ** 0.5 / 2 * a
    root2 = -b - d ** 0.5 / 2 * a
    return root1, root2

a = int(input('Enter coefficient of x^2: '))
b = int(input('Enter coefficient of x: '))
c = int(input('Enter last term: '))
r1, r2 = solveQuadraticEquation(a, b, c)
print('Root1: ', r1, '\nRoot2: ', r2)
