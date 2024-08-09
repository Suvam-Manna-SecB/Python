# Write a program to check whether a number is palindrome or not.

num = int(input('Enter Number: '))
copy = num
rev = 0
while num>0:
    rem = num%10
    rev = rev * 10 + rem
    num = num//10

if rev==copy:
    print('Palindrome Number')
else:
    print('Not a Palindrome Number')
