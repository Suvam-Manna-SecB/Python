# Write a function to calculate the power of a number using recursion
def power(a, b):
    if b == 1:
        return a
    else:
        power(a*a, b-1)

a= int(input('Enter Base: '))
b = int(input('Enter Power: '))
print('{} to the power of {} = {}'.format(a, b, power(a, b)))
