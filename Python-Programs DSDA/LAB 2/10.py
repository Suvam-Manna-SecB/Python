# Write a program in python to check if a number is Krishnamurthy number.
import math
n = int(input('Enter Number: '))
copy = n
sum = 0
while n>0:
    rem = n%10
    sum = sum + math.factorial(rem)
    n = n // 10

if copy==sum:
    print('Krishnamurthy Number')
else:
    print('Not a Krishnamurthy Number')
