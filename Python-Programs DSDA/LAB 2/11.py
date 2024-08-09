# Write a program in python to find the sum of digits of a number
n = int(input('Enter Number: '))
sum = 0
copy = n
while n>0:
    rem = n % 10
    sum = sum + rem
    n = n // 10
n = copy
print('Sum of Digits of {} = {}'.format(n, sum))
        
