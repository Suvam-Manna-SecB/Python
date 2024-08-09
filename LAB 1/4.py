# Write a program to reverse a number.

n = int(input('Enter Number: '))
rev = 0
while(n > 0):
    rem = n % 10
    rev = rev * 10 + rem
    n = n//10

print('Reversed Number: ', rev)
