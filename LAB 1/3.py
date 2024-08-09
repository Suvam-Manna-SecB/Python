# Write a program to check whether given year is leap year or not.

year = int(input('Enter Year: '))
flag = False
if year % 400 == 0:
    flag = True
elif year % 100 == 0:
    flag = False
elif year % 4 == 0:
    flag = True

if flag:
    print('Leap Year')
else:
    print('Not a Leap Year')
