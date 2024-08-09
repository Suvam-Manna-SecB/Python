# Write a python program that prompts the user to enter a base number
# and an exponent, and then calculates the power of the base to the
# exponent. The program should not use the exponentiation operator(**)
# or the math.pow() function.
a = int(input('Enter Base Number: '))
b = int(input('Enter Exponent: '))
val = a
for i in range(1, b):
    val = val * a

print(val)
